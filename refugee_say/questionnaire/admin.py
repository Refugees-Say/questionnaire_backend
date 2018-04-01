from django.contrib import admin
from .models import Questionnaire, QuestionOrder
from .forms import QuestionOrderForm


@admin.register(QuestionOrder)
class QuestionOrder(admin.ModelAdmin):
    form =  QuestionOrderForm

admin.site.register(Questionnaire)
