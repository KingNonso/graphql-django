from django.contrib import admin
from . import models


@admin.register(models.Link)
class LinksAdmin(admin.ModelAdmin):
    list_display = ['url', 'description']
