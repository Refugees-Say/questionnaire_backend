from rest_framework import serializers

from refugee_say.questionnaire.models import Questionnaire
from refugee_say.users.models import User
from .models import Response


class ResponseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    questionnaire = serializers.PrimaryKeyRelatedField(queryset=Questionnaire.objects.all())

    class Meta:
        model = Response
        fields = ('id', 'response', 'user', 'questionnaire', 'created_at', 'updated_at')
