
from django.contrib import admin
from django.urls import path

from resume_checker.views import JobDescriptionAPI,AnalyzeResumeAPI


urlpatterns = [
    path('api/jobs/', JobDescriptionAPI.as_view(), name='job_description_api'),
    path('api/resume/', AnalyzeResumeAPI.as_view(), name='analyze_resume_api'),
]
