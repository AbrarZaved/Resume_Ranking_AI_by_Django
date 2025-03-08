from django.contrib import admin
from django.contrib.auth.models import Group

from resume_checker.models import JobDescription, Resume

# Register your models here.

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'resume')
    search_fields = ('id', 'resume')

@admin.register(JobDescription)
class JobDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'job_description')
    search_fields = ('id', 'job_title', 'job_description')

admin.site.unregister(Group)