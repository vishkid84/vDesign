from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class PowerPointProject(models.Model):
    PPT_CHOICES = ((0, 'Check for alignment issues, fix fonts and font sizes'),
                    (1, 'Change text/table to other layouts to represent better'),
                    (2, 'Use appropriate cover image and divider image'),
                    (3, 'Use appropriate images and icons/pictograms'),
                    (4, 'Add basic animations/transitions'),
                    (5, 'Convert to an interactive PDF'),
                    (6, 'Develop a theme/style for the document and design the document based on the theme'),
                    (7, 'Change layouts to high-end infographics by adding vectors/pictograms'),
                    (8, 'Use high-end complex animations to represent the data'))

    client = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    your_full_name = models.CharField(max_length=300)
    project_name = models.CharField(max_length=250)
    project_description = models.TextField()
    requirements = MultiSelectField(choices=PPT_CHOICES)
    quote = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
