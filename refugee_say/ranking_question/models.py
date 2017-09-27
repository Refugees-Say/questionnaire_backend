from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.utils.translation import ugettext_lazy as _

from refugee_say.question.models import AbstractQuestion


class RankingQuestion(AbstractQuestion):
    multiplier = ArrayField(models.FloatField(_('Multiplier'), default=1.0))

    def type(self):
        return 'rank'

    def __str__(self):
        return self.question

    @classmethod
    def validate_answer(cls, answer):
        return True
