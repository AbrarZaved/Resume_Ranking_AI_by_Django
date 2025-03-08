from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
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
            return Response({"status": True, "message": "Resume Analyzed", "data": data})
        except Exception as e:
            return Response({"status": False, "message": str(e)})
