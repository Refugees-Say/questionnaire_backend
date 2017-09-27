from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class AbstractQuestion(models.Model):
    question = models.CharField(_('Question'), max_length=255)
    description = models.TextField(_('Description'), null=True, blank=True)
    language = models.CharField(_('Language'), max_length=10, default=settings.LANGUAGE_CODE, choices=settings.LANGUAGES)
    # type = models.CharField()

    def __str__(self):
        return self.question

    class Meta:
        abstract = True

    @property
    def type(self):
        raise NotImplementedError(_('Type not implemented'))

    @classmethod
    def validate_answer(cls, answer):
        raise NotImplementedError(_('Need to provide an implementation to validate answers received form users'))
