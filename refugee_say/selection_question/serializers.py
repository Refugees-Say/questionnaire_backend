from rest_framework import serializers

from .models import SelectionQuestion


class SelectionQuestionSerializer(serializers.ModelSerializer):
    choice_set = serializers.StringRelatedField(many=True, read_only=True, allow_null=True)

    class Meta:
        model = SelectionQuestion
        fields = ('id', 'question', 'language', 'description', 'choice_set')
        depth = 1
