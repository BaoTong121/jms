from django.contrib import admin

# Register your models here.

from .models import Assets


@admin.register(Assets)
class AssetAdmin(admin.ModelAdmin):
    pass
