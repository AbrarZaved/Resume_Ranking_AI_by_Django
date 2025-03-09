from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class JobDescription(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()

    def __str__(self):
        return self.job_title


class Resume(models.Model):
    job_title = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
