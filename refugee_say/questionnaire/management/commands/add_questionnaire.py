import csv
import re
from django.core.management.base import BaseCommand, CommandError
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from refugee_say.questionnaire.models import Questionnaire, QuestionOrder
from refugee_say.radio_question.models import RadioQuestion
from refugee_say.selection_question.models import SelectionQuestion
from refugee_say.ranking_question.models import RankingQuestion
from refugee_say.choice.models import Choice


class Command(BaseCommand):
    help = 'Adding a new questionnaire from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
        parser.add_argument('--delimiter', type=str, default=',')

    def handle(self, *args, **options):
        f = options['csv_file']
        assert len(options['delimiter']) == 1
        with open(options['csv_file']) as csv_file:
            questions = csv.reader(csv_file, delimiter=options['delimiter'])
            description, language = next(questions)
            questionnaire = Questionnaire(description=description, language=language)
            val = URLValidator()
            questionnaire.save()
            classes = {
                'radio': RadioQuestion,
                'selection': SelectionQuestion,
                # 'ranking': RankingQuestion,
            }
            for order, line in enumerate(questions, 1):
                cls, question, *choices = line
                question = re.sub('\s+', ' ', question)
                cls_name = re.sub('\s+', '', cls.lower())
                try:
                    cls = classes[cls_name]
                    obj = cls(question=question, language=language)
                except KeyError:
                    obj = RankingQuestion(question=question, language=language, multiplier=[1])
                obj.save()
                qo = QuestionOrder(order=order, questionnaire=questionnaire)
                if cls_name == 'radio':
                    qo.radio = obj
                elif cls_name == 'selection':
                    qo.selection = obj
                elif cls_name == 'ranking':
                    qo.rank = obj
                else:
                    raise CommandError("Couldn't find a matching question type (Got {})".format(cls_name))
                qo.save()
                for i, choice in enumerate(choices):
                    if i % 2 != 0: continue
                    url = re.sub('\s', '', choices[i+1])
                    choice = re.sub('\s+', ' ', choice)
                    try:
                        val(url)
                    except ValidationError as e:
                        if url == 'null' or url == '':
                            url = None
                        else:
                            raise ValidationError(e)
                    c = Choice(choice=choice, image_url=url)
                    c.save()
                    obj.choice_set.add(c)
                    obj.save()
                print(cls_name, question, choices)
        self.stdout.write(self.style.SUCCESS('Successfully created a questionnaire'))
