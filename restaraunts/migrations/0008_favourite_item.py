# Generated by Django 2.0.2 on 2018-03-01 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaraunts', '0007_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaraunts.Item'),
        ),
    ]
