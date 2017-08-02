from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from refugee_say.users.models import User

# Create your models here.
class Type(models.Model):
    type = models.CharField(_('Type'), max_length=40)

    def __str__(self):
        return self.type


class Question(models.Model):
    question = models.CharField(_('Question'), max_length=255)
    description = models.TextField(_('Description'), null=True, blank=True)

    order = models.PositiveSmallIntegerField(default=1)

    language = models.CharField(_('Language'), max_length=10, default=settings.LANGUAGE_CODE,
                                choices=settings.LANGUAGES)

    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.question

    class Meta:
        unique_together = ('language', 'order', )
