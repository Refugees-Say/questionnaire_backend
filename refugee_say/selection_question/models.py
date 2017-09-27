from refugee_say.question.models import AbstractQuestion


class SelectionQuestion(AbstractQuestion):

    def type(self):
        return 'selection'

    def __str__(self):
        return self.question

    @classmethod
    def validate_answer(cls, answer):
        return True
