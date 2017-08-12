from rest_framework import serializers

from refugee_say.questionnaire.models import Questionnaire
from .models import Response


class ResponseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    questionnaire = serializers.PrimaryKeyRelatedField(queryset=Questionnaire.objects.all())

    class Meta:
        model = Response
        fields = ('id', 'response', 'user', 'questionnaire', 'created_at', 'updated_at')
        read_only_fields = ('user', )
