from django.db import models
from django.utils.translation import ugettext_lazy as _
from django import get_version
from django.contrib.auth import get_user_model as auth_model
from django.conf import settings
from refugee_say.questionnaire.models import Questionnaire

get_user_model = lambda : auth_model() if int(get_version().split('.')[1]) > 10 else settings.AUTH_USER_MODEL

class Response(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)

    response = models.TextField(_('Response'))
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(_('Created time'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Last updated time'), auto_now=True)

    def __str__(self):
        return self.user.username
