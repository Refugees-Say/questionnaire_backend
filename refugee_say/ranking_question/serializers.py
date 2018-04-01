from rest_framework import serializers

from .models import RankingQuestion
from refugee_say.choice.serializers import ChoiceSerializer


class RankingQuestionSerializer(serializers.ModelSerializer):
    # choices = serializers.StringRelatedField(source='choice_set', many=True, read_only=True, allow_null=True)
    choices = ChoiceSerializer(source='choice_set', many=True, read_only=True, allow_null=True)

    class Meta:
        model = RankingQuestion
        fields = ('id', 'question', 'description', 'language', 'choices', 'type')
        read_only_fields = ('type', )
        depth = 3
