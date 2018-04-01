from rest_framework import serializers

from refugee_say.choice.serializers import ChoiceSerializer
from .models import SelectionQuestion

class SelectionQuestionSerializer(serializers.ModelSerializer):
    #choices = serializers.StringRelatedField(source='choice_set', many=True, read_only=True, allow_null=True)
    choices = ChoiceSerializer(source='choice_set', many=True, read_only=True, allow_null=True)

    class Meta:
        model = SelectionQuestion
        fields = ('id', 'question', 'language', 'description', 'choices', 'type')
        read_only_fields = ('type', )
        depth = 3
