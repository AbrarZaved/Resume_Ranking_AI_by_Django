from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from resume_checker.views import JobDescriptionAPI, AnalyzeResumeAPI


urlpatterns = [
    path("api/jobs/", JobDescriptionAPI.as_view(), name="job_description_api"),
    path("api/resume/", AnalyzeResumeAPI.as_view(), name="analyze_resume_api"),
    path("", views.index, name="index"),
    path("check_resume", csrf_exempt(views.check_resume), name="check_resume"),
]
