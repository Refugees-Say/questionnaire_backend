from django.db import IntegrityError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import QuestionOrder, Questionnaire
from refugee_say.radio_question.models import RadioQuestion
from refugee_say.ranking_question.models import RankingQuestion
from refugee_say.selection_question.models import SelectionQuestion


class QuestionRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        print(type(value))
        if isinstance(value, RadioQuestion):
            return super().to_representation(value)
        if isinstance(value, RankingQuestion):
            return super().to_representation(value)
        if isinstance(value, SelectionQuestion):
            return super().to_representation(value)
        return super().to_representation(value)
        # raise Exception(_('Unexpected type of tagged object'))

    def to_internal_value(self, data):
        super().to_internal_value(data)


class QuestionnaireSerializer_(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(queryset=Questionnaire.objects.values_list('radios', 'ranks', 'selections'))

    def get_questions(self, obj: Questionnaire):
        questions = QuestionOrder.objects.filter(questionnaire=obj).order_by('order')
        print(questions)
        # questions = []
        # for item in obj.radios:
        #     questions.append(item)
        # for item in obj.ranks:
        #     questions.append(item)
        # for item in obj.selections:
        #     questions.append(item)
        return questions

    class Meta:
        model = Questionnaire
        fields = ('id', 'description', 'created_at', 'updated_at', 'language', 'questions', )
        read_only_fields = ('questions', )
        depth = 1


class QuestionOrderSerializer(serializers.ModelSerializer):
    radio = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=RadioQuestion.objects.all())
    rank = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=RankingQuestion.objects.all())
    selection = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=SelectionQuestion.objects.all())
    questionnaire = serializers.PrimaryKeyRelatedField(queryset=Questionnaire.objects.all())

    def create(self, validated_data):
        try:
            order = super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(_('Order and language has to be unique per questionnaire'))
        return order

    def validate(self, attrs):
        s = {
            attrs.get('rank'),
            attrs.get('radio'),
            attrs.get('selection'),
             }
        s -= {None}
        s = list(s)
        if len(s) == 1 and isinstance(s[0], (RadioQuestion, RankingQuestion, SelectionQuestion)):
            if s[0].language == attrs.get('questionnaire').language:
                return super().validate(attrs)
            raise  serializers.ValidationError(_("Languages didn't match"))
        raise serializers.ValidationError(_('Order needs to be assigned to only one of the questions'))

    class Meta:
        depth = 1
        model = QuestionOrder
        fields = ('order', 'rank', 'radio', 'selection', 'questionnaire')



class QuestionnaireSerializerV2(serializers.ModelSerializer):

    questions = QuestionOrderSerializer(source='questionorder_set', many=True)

    class Meta:
        model = Questionnaire
        fields = ('id', 'description', 'created_at', 'updated_at', 'language', 'questions', 'questions')


class QuestionnaireSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    language = serializers.ChoiceField(default=settings.LANGUAGE_CODE, choices=settings.LANGUAGES)
    description = serializers.CharField(allow_blank=True)
    # questions = serializers.ListField(allow_null=True, allow_empty=True)
    questions = QuestionOrderSerializer(many=True, allow_null=True)
        # serializers.PrimaryKeyRelatedField(allow_null=True, read_only=True)

    def create(self, validated_data):
        validated_data.pop('questions')
        return Questionnaire.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    def to_representation(self, instance):
        print('To representation')
        print(instance.questions)
        print(JSONRenderer().render(QuestionOrderSerializer(instance.questions, many=True).data))
        # instance.questions = JSONRenderer().render(QuestionOrderSerializer(instance.questions, many=True).data)
        return super().to_representation(instance)
