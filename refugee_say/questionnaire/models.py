from django.db import models

from refugee_say.question.models import Question
from refugee_say.users.models import User

# Create your models here.
class Questionnaire(models.Model):

    questions = models.ManyToManyField(Question)
    # answers = models.ManyToManyField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
