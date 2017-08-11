from refugee_say.question.models import AbstractQuestion


class RankingQuestion(AbstractQuestion):

    def type(self):
        return 'rank'

    def __str__(self):
        return self.question
