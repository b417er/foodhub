from django.db import models

class Restaraunt(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    opening = models.DateTimeField(auto_now=True, auto_now_add=False)
    closing = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
