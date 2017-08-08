from refugee_say.question.models import AbstractQuestion


class SelectionQuestion(AbstractQuestion):


    def __str__(self):
        return self.question
