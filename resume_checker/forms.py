from django import forms
from django.forms import widgets

from resume_checker.models import Resume


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ResumeForm(forms.ModelForm):
    resume = MultipleFileField(
        label="Resume(s)",
        widget=MultipleFileInput(
            attrs={
                "class": "block w-full px-4 py-3 text-base text-gray-700 border border-gray-300 rounded-lg cursor-pointer bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all hover:border-gray-400",
                "accept": ".pdf",
            }
        ),
    )

    class Meta:
        model = Resume
        fields = ["job_title", "resume"]
        labels = {"job_title": "Job Title", "resume": "Resume(s)"}
        widgets = {
            "job_title": widgets.Select(
                attrs={
                    "class": "block w-full px-4 py-4 text-base border border-gray-300 rounded-lg shadow-sm bg-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all hover:border-gray-400"
                }
            ),
        }
