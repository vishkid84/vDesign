from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['category',
                  'name',
                  'description',
                  'paragraph',
                  'thumb_image',
                  'image_one',
                  'image_two',
                  'image_three'
                  ]
