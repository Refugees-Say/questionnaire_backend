from rest_framework import serializers

from .models import Choice

from refugee_say.radio_question.models import RadioQuestion
from refugee_say.ranking_question.models import RankingQuestion
from refugee_say.selection_question.models import SelectionQuestion



# class TypeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Type
#         fields = ('type', )


class ChoiceSerializer(serializers.ModelSerializer):
    radio = serializers.PrimaryKeyRelatedField(many=False, allow_null=True, queryset=RadioQuestion.objects.all())
    rank = serializers.PrimaryKeyRelatedField(many=False, allow_null=True, queryset=RankingQuestion.objects.all())
    selection = serializers.PrimaryKeyRelatedField(many=False, allow_null=True, queryset=SelectionQuestion.objects.all())
    # type = serializers.StringRelatedField(many=False, source='type')

    def validate(self, data):
        super().validate(data)
        rank = data.get('rank')
        radio = data.get('radio')
        selection = data.get('selection')

        if (isinstance(radio, RadioQuestion) and rank is None and selection is None) \
            or (radio is None and isinstance(rank, RankingQuestion) and selection is None) \
            or (radio is None and rank is None and isinstance(selection, SelectionQuestion)):
            return True
        raise serializers.ValidationError('Choice can be assigned to one question at a time')

    class Meta:
        model = Choice
        fields = ('id', 'choice', 'image_url', 'rank', 'radio', 'selection', )
        depth = 3
