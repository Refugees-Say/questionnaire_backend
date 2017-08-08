from rest_framework import serializers

from .models import Choice, Type

from refugee_say.radio_question.serializers import RadioQuestion, RadioQuestionSerializer
from refugee_say.ranking_question.serializers import RankingQuestion, RankingQuestionSerializer
from refugee_say.selection_question.serializers import SelectionQuestion, SelectionQuestionSerializer



class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('type', )


class ChoiceSerializer(serializers.ModelSerializer):
    radio = serializers.PrimaryKeyRelatedField(many=False, allow_null=True, queryset=RadioQuestion.objects.all())
    rank = serializers.PrimaryKeyRelatedField(many=False, allow_null=True, queryset=RankingQuestion.objects.all())
    selection = serializers.PrimaryKeyRelatedField(many=False, allow_null=True, queryset=SelectionQuestion.objects.all())
    type = serializers.PrimaryKeyRelatedField(many=False, queryset=Type.objects.all())

    def validate(self, data):
        rank = data.get('rank')
        radio = data.get('radio')
        selection = data.get('selection')

        if (isinstance(radio, RadioQuestion) and rank is None and selection is None) \
            or (radio is None and isinstance(rank, RankingQuestion) and selection is None) \
            or (radio is None and rank is None and isinstance(selection, SelectionQuestion)):
            return super().validate(data)
        raise serializers.ValidationError('Choice can be assigned to one question at a time')

    class Meta:
        model = Choice
        fields = ('id', 'choice', 'type', 'rank', 'radio', 'selection', )
        depth = 1
