from django.db import models

class Post(models.Model):
    title       = models.CharField(max_length=155)
    description = models.TextField()
    created_at  = models.DateField()

    def __str__(self):
        return '#' + str(self.id) + ' - ' + self.title + '   @' + str(self.created_at)
