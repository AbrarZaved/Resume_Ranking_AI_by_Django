from django.db import models

# Create your models here.


class Resume(models.Model):
    resume = models.FileField(upload_to="resumes/")


class JobDescription(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()

    def __str__(self):
        return self.job_title
