from django import forms
from .models import PowerPointProject

class PowerPointProjectForm(forms.ModelForm):
    class Meta:
        model = PowerPointProject
        fields = ['project_name',
                  'project_description',
                  'requirements',
                  ]
