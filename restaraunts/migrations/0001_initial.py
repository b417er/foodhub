# Generated by Django 2.0.2 on 2018-02-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaraunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('opening', models.DateTimeField(auto_now=True)),
                ('closing', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
