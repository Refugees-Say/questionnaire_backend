from django.db import models
from django.utils.translation import ugettext_lazy as _

from refugee_say.choice.models import Choice
from refugee_say.city.models import City


class Score(models.Model):
    value = models.IntegerField(_('value'), default=0)

    choice = models.ForeignKey(Choice)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.value
