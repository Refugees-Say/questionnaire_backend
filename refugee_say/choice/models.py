from django.db import models
from django.utils.translation import ugettext_lazy as _


class Type(models.Model):
    type = models.CharField(_('Choice Type'), max_length=200)

    def __str__(self):
        return self.type


class Choice(models.Model):
    rank = models.ForeignKey('ranking_question.RankingQuestion', null=True, blank=True)
    radio = models.ForeignKey('radio_question.RadioQuestion', null=True, blank=True)
    selection = models.ForeignKey('selection_question.SelectionQuestion', null=True, blank=True)

    choice = models.TextField(_('Choice'))
    type = models.ForeignKey('Type')

    def __str__(self):
        return self.choice
