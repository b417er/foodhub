# Generated by Django 2.0.2 on 2018-03-04 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaraunts', '0009_auto_20180301_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaraunt',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
