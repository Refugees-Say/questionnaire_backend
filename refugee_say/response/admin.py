from django.contrib import admin

from .models import Response


@admin.register(Response)
class ResponseAdminSite(admin.ModelAdmin):
    pass
