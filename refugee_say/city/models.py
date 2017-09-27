from django.db import models
from django.utils.translation import ugettext_lazy as _


class City(models.Model):
    name = models.CharField(_('City'), max_length=255)

    def __str__(self):
        return self.name
