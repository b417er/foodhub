# Generated by Django 2.0.2 on 2018-02-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaraunts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaraunt',
            name='opening',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
