from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from resume_checker.forms import ResumeForm
from resume_checker.models import JobDescription, Resume
from resume_checker.serializer import JobDescriptionSerializer, ResumeSerializer
from .analyzer import process_resume


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
        form = ResumeForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                job_id = request.POST["job_title"]
                resume_instance = form.save()
            file_path = resume_instance.resume.path
            job_desc = JobDescription.objects.get(id=job_id).job_description
        except Exception as e:
            print(e)

        data = process_resume(file_path, job_desc)
        return render(request, "partials/result.html", {"data": data})

    form = ResumeForm()
    return render(request, "index.html", {"form": form})
