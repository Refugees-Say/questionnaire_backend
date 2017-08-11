from rest_framework import serializers

from .models import RankingQuestion


class RankingQuestionSerializer(serializers.ModelSerializer):
    choices = serializers.StringRelatedField(source='choice_set', many=True, read_only=True, allow_null=True)

    class Meta:
        model = RankingQuestion
        fields = ('id', 'question', 'description', 'language', 'choices')
        depth = 1
