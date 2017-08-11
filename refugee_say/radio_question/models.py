from refugee_say.question.models import AbstractQuestion


class RadioQuestion(AbstractQuestion):

    def type(self):
        return 'radio'

    def __str__(self):
        return self.question
