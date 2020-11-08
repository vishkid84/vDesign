from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class PowerPointProject(models.Model):
    PPT_CHOICES = (('Alignment', 'Check for alignment issues, fix fonts and font sizes'),
                    ('Table conversion', 'Change text/table to other layouts to represent better'),
                    ('Cover and divider images', 'Use appropriate cover image and divider image'),
                    ('Icons', 'Use appropriate images and icons/pictograms'),
                    ('Basic animation', 'Add basic animations/transitions'),
                    ('Interactive pdf', 'Convert to an interactive PDF'),
                    ('Themed', 'Develop a theme/style for the document and design the document based on the theme'),
                    ('Infographics', 'Change layouts to high-end infographics by adding vectors/pictograms'),
                    ('Complex animations', 'Use high-end complex animations to represent the data'))

    client = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_description = models.TextField()
    requirements = MultiSelectField(choices=PPT_CHOICES)

    def __str__(self):
        return self.project_name


class PowerPointQuote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(PowerPointProject, related_name='powerpoint', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username