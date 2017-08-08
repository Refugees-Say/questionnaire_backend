from django.contrib import admin

from .models import RadioQuestion


@admin.register(RadioQuestion)
class RadioQuestionAdminSite(admin.ModelAdmin):
    pass
