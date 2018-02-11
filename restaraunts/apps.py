from django.apps import AppConfig
from django.contrib import admin
from .models import foodhub

class PostModelAdmin(admin.ModelAdmin):
    class Meta:
        model = restaraunts

admin.site.register(restaraunts, PostModelAdmin)


class RestarauntsConfig(AppConfig):
    name = 'restaraunts'
