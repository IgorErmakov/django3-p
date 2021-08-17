from django.db import models
#from django.db.models import Model

class Project(models.Model):
    title       = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image       = models.ImageField(upload_to = 'portfolio/images/')
    url         = models.URLField(blank=True)
    #description = models.TextField()

    def __str__(self):
        return self.title
