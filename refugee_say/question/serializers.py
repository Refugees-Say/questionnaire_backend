import logging
from rest_framework import serializers

from .models import Question, Type


class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(many=False, queryset=Type.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Question
        fields = ('id', 'question', 'description', 'language', 'order', 'type', 'user')
        depth = 1

    def create(self, validated_data):
        return Question.objects.create(**validated_data)


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'type')


# class CreateUserSerializer(serializers.ModelSerializer):
#
#     def create(self, validated_data):
#         # call create_user on user object. Without this
#         # the password will be stored in plain text.
#         user = User.objects.create_user(**validated_data)
#         return user
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password', 'auth_token')
#         read_only_fields = ('auth_token',)
#         extra_kwargs = {'password': {'write_only': True}}
