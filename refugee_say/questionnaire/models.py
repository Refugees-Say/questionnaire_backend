from django.db import models, IntegrityError
from django.db.models import Q
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver

from django.conf import settings

# from refugee_say.question.models import Question

from refugee_say.radio_question.models import RadioQuestion
from refugee_say.ranking_question.models import RankingQuestion
from refugee_say.selection_question.models import SelectionQuestion


class QuestionOrder(models.Model):
    order = models.SmallIntegerField(_('Question order'), default=1)
    # question = models.ForeignKey('Question', on_delete=models.DO_NOTHING)
    radio = models.ForeignKey(RadioQuestion, on_delete=models.DO_NOTHING, null=True)
    rank = models.ForeignKey(RankingQuestion, on_delete=models.DO_NOTHING, null=True)
    selection = models.ForeignKey(SelectionQuestion, on_delete=models.DO_NOTHING, null=True)
    questionnaire = models.ForeignKey('Questionnaire', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.order)


@receiver(pre_save, sender=QuestionOrder)
def question_order_checker(sender, instance, *args, **kwargs): # raw, using, update_fields):
    q = {
        'radio__language': instance.radio.language if hasattr(instance.radio, 'language') else None,
        'rank__language': instance.rank.language if hasattr(instance.rank, 'language') else None,
        'selection__language': instance.selection.language if hasattr(instance.selection, 'language') else None,
    }
    try:
        sender.objects.get(Q(questionnaire=instance.questionnaire), Q(order=instance.order),
                           Q(radio__language=q['radio__language']) |
                           Q(rank__language=q['rank__language']) |
                           Q(selection__language=q['selection__language']))
    except sender.DoesNotExist:
        return True
    except sender.MultipleObjectsReturned:
        pass
    raise IntegrityError(_('Language and order has to be unique: language = {language}, order = {order}').format(
        language=q.get('radio__language') or q.get('rank__language') or q.get('selection__language'),
        order=instance.order,
    ))


class Questionnaire(models.Model):

    radios = models.ManyToManyField(RadioQuestion, through=QuestionOrder)
    ranks = models.ManyToManyField(RankingQuestion, through=QuestionOrder)
    selections = models.ManyToManyField(SelectionQuestion, through=QuestionOrder)
    language = models.CharField(_('Language'), max_length=10, default=settings.LANGUAGE_CODE,
                                choices=settings.LANGUAGES)
    # answers = models.ManyToManyField()

    description = models.TextField(_('Description'), null=True, blank=True)
    created_at = models.DateTimeField(_('Creation time'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Last updated time'), auto_now=True)


    def __str__(self):
        return self.description
