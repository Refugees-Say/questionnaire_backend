from django.contrib import admin

from .models import Choice, Type


@admin.register(Choice)
class ChoiceAdminSite(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdminSite(admin.ModelAdmin):
    pass
