from django.contrib import admin

# Register your models here.

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(models.ModelAdmin):
    list_display = ['user','date_of_birth','photo']
    raw_id_fields = ['user']