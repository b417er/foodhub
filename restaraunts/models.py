from django.db import models

class Restaraunt(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    opening = models.DateTimeField()
    closing = models.DateTimeField()

    def __str__(self):
        return self.name

# Create your models here.
