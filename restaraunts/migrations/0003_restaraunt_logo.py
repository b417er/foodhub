# Generated by Django 2.0.2 on 2018-02-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaraunts', '0002_auto_20180213_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaraunt',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
