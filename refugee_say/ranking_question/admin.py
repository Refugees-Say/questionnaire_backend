from django.contrib import admin

from .models import RankingQuestion


@admin.register(RankingQuestion)
class RankingQuestionAdminSite(admin.ModelAdmin):
    pass
