from django.db import models

class Restaraunt(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    opening = models.DateTimeField(auto_now_add = True)
    closing = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

# Create your models here.
