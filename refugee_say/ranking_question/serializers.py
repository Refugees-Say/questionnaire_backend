from rest_framework import serializers

from .models import RankingQuestion


class RankingQuestionSerializer(serializers.ModelSerializer):
    choice_set = serializers.StringRelatedField(many=True, read_only=True, allow_null=True)

    class Meta:
        model = RankingQuestion
        fields = ('id', 'question', 'description', 'language', 'choice_set')
        depth = 1
