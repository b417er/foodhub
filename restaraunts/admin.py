from django.contrib import admin
from .models import Restaraunt

class RestarauntModelAdmin(admin.ModelAdmin):
	list_display = ["id","name"]
	class Meta:
		model = Restaraunt

admin.site.register(Restaraunt, RestarauntModelAdmin)

# Register your models here.
