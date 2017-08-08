from django.contrib import admin

from .models import SelectionQuestion


@admin.register(SelectionQuestion)
class SelectionQuestionAdminSite(admin.ModelAdmin):
    pass
