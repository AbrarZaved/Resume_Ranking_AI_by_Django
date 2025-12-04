from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from resume_checker.forms import ResumeForm
from resume_checker.models import JobDescription, Resume
from resume_checker.serializer import JobDescriptionSerializer, ResumeSerializer
from .analyzer import process_resume, process_multiple_resumes


class JobDescriptionAPI(APIView):
    def get(self, request):
        queryset = JobDescription.objects.all()
        serialize = JobDescriptionSerializer(queryset, many=True)
        return Response({"status": 200, "data": serialize.data})


class AnalyzeResumeAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            if not data.get("job_description"):
                return Response(
                    {
                        "status": False,
                        "message": "job_description is required",
                        data: {},
                    }
                )

            serializer = ResumeSerializer(data=data)
            if not serializer.is_valid():
                return Response(
                    {
                        "status": False,
                        "message": serializer.errors,
                    }
                )

            serializer.save()
            _data = serializer.data
            resume_instance = Resume.objects.get(id=_data.get("id"))
            resume_path = resume_instance.resume.path
            data = process_resume(
                resume_path,
                JobDescription.objects.get(
                    id=data.get("job_description")
                ).job_description,
            )
            return Response(
                {"status": True, "message": "Resume Analyzed", "data": data}
            )
        except Exception as e:
            return Response({"status": False, "message": str(e)})


def index(request):
    form = ResumeForm()
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request, "index.html", {"form": form})


def check_resume(request):
    if request.method == "POST":
        try:
            job_id = request.POST.get("job_title")
            files = request.FILES.getlist("resume")

            if not files:
                return render(
                    request,
                    "partials/result.html",
                    {"error": "No resume files uploaded"},
                )

            job_desc = JobDescription.objects.get(id=job_id).job_description

            # Process multiple resumes
            resume_paths = []
            resume_instances = []

            for file in files:
                # Create a resume instance for each file
                resume_instance = Resume.objects.create(
                    job_title_id=job_id, resume=file
                )
                resume_instances.append(resume_instance)
                resume_paths.append(resume_instance.resume.path)

            # Process all resumes
            results = process_multiple_resumes(resume_paths, job_desc)

            # Normalize and format scores
            for result in results:
                if "rank" in result and not result.get("error"):
                    rank = result["rank"]
                    # Convert to float
                    if isinstance(rank, str):
                        rank = rank.replace("%", "").strip()
                    try:
                        score = float(rank)
                        # If score is between 0 and 1, convert to percentage
                        if 0 <= score <= 1:
                            score = score * 100
                        # Format with percentage sign
                        result["rank"] = f"{score:.0f}%"
                    except (ValueError, TypeError):
                        result["rank"] = "0%"

            # Sort results by score (descending)
            def get_score(x):
                rank = x.get("rank", "0%")
                if isinstance(rank, str):
                    return float(rank.replace("%", ""))
                return float(rank) if rank else 0

            results.sort(key=get_score, reverse=True)

            return render(
                request,
                "partials/result.html",
                {"results": results, "total_resumes": len(results)},
            )

        except Exception as e:
            print(f"Error: {e}")
            return render(request, "partials/result.html", {"error": str(e)})

    form = ResumeForm()
    return render(request, "index.html", {"form": form})
