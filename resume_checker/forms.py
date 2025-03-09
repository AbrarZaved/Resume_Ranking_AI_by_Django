from django import forms
from django.forms import widgets

from resume_checker.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["job_title", "resume"]
        labels = {"job_title": "Job Title", "resume": "Resume"}
        widgets = {
            "job_title": widgets.Select(
                attrs={
                    "class": "mt-1 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
                }
            ),
            "resume": widgets.FileInput(
                attrs={
                    "class": "mt-1 block w-full border border-gray-300 rounded-lg p-2 bg-gray-50 focus:ring-indigo-500 focus:border-indigo-500",
                    "accept": ".pdf",
                }
            ),
        }
