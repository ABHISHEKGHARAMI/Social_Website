# Generated by Django 5.0.4 on 2024-05-01 16:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['created']},
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['-created'], name='images_imag_created_d57897_idx'),
        ),
    ]
