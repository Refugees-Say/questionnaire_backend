from refugee_say.question.models import AbstractQuestion


class RadioQuestion(AbstractQuestion):


    def __str__(self):
        return self.question
