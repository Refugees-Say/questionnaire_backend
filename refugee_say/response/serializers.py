import json

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from refugee_say.questionnaire.models import Questionnaire
from .models import Response

from refugee_say.radio_question.models import RadioQuestion
from refugee_say.ranking_question.models import RankingQuestion
from refugee_say.selection_question.models import SelectionQuestion


class ResponseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    questionnaire = serializers.PrimaryKeyRelatedField(queryset=Questionnaire.objects.all())

    def validate(self, attrs):
        data = super().validate(attrs)
        try:
            response = json.loads(data.get('response'))
        except json.JSONDecodeError:
            raise serializers.ValidationError(_('response field has to be a JSON decodable'))
        questionnaire = data.get('questionnaire')
        types = {'rank': RankingQuestion, 'radio': RadioQuestion, 'selection': SelectionQuestion}
        for answer in response.get('answers'):
            if answer.get('type') in types.keys():
                question_cls = types[answer.get('type')]
                if question_cls.validate_answer(answer=answer): continue
                raise serializers.ValidationError(_("One of the question didn't validate class {class}, {data}").format(
                    question_cls, answer))
            else:
                raise serializers.ValidationError(_('Expected the following list of {types}').format(types=types))
        return data

    class Meta:
        model = Response
        fields = ('id', 'response', 'user', 'questionnaire', 'created_at', 'updated_at')
        read_only_fields = ('user', )
