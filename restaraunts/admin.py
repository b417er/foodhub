from django.contrib import admin
from .models import Restaraunt, Item

class RestarauntModelAdmin(admin.ModelAdmin):
	list_display = ["id","name"]
	class Meta:
		model = Restaraunt

admin.site.register(Restaraunt, RestarauntModelAdmin)

class ItemModelAdmin(admin.ModelAdmin):
	list_display = ["id","name"]
	class Meta:
		model = Item

admin.site.register(Item, ItemModelAdmin)

# Register your models here.
