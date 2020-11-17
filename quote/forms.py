from django import forms
from .models import PowerPointProject

class PowerPointProjectForm(forms.ModelForm):
    class Meta:
        model = PowerPointProject
        fields = ['your_full_name',
                  'project_name',
                  'requirements',
                  ]
