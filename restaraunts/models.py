from django.db import models
from django.contrib.auth.models import User



class Restaraunt(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    logo = models.ImageField(null=True)
    opening = models.TimeField()
    closing = models.TimeField()  
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Item(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=3)
	restaraunt = models.ForeignKey(Restaraunt, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class FavouriteRestaraunt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaraunt = models.ForeignKey(Restaraunt, on_delete=models.CASCADE)

class FavouriteItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, default=1, on_delete=models.CASCADE)

    

# Create your models here.
