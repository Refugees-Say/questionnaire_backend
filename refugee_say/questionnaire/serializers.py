from django.db import IntegrityError
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from .models import QuestionOrder, Questionnaire

from refugee_say.radio_question.models import RadioQuestion
from refugee_say.ranking_question.models import RankingQuestion
from refugee_say.selection_question.models import SelectionQuestion

from refugee_say.radio_question.serializers import RadioQuestionSerializer
from refugee_say.ranking_question.serializers import RankingQuestionSerializer
from refugee_say.selection_question.serializers import SelectionQuestionSerializer


class QuestionOrderSerializer(serializers.ModelSerializer):
    radio = RadioQuestionSerializer(read_only=True)
    rank = RankingQuestionSerializer(read_only=True)
    selection = SelectionQuestionSerializer(read_only=True)

    def create(self, validated_data):
        try:
            order = super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(_('Order and language has to be unique per questionnaire'))
        return order

    def validate(self, attrs):
        s = {
            attrs.get('rank'),
            attrs.get('radio'),
            attrs.get('selection'),
             }
        s -= {None}
        s = list(s)
        if len(s) == 1 and isinstance(s[0], (RadioQuestion, RankingQuestion, SelectionQuestion)):
            if s[0].language == attrs.get('questionnaire').language:
                return super().validate(attrs)
            raise  serializers.ValidationError(_("Languages didn't match"))
        raise serializers.ValidationError(_('Order needs to be assigned to only one of the questions'))

    class Meta:
        depth = 1
        model = QuestionOrder
        fields = ('order', 'rank', 'radio', 'selection', )



class QuestionnaireSerializer(serializers.ModelSerializer):
    questions = QuestionOrderSerializer(source='questionorder_set', many=True)

    class Meta:
        model = Questionnaire
        fields = ('id', 'description', 'created_at', 'updated_at', 'language', 'questions', 'questions')
        depth = 4
