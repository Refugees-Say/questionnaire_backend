from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, permission_classes

from .permissions import IsAdminOrReadOnly
# from .serializers import QuestionSerializer, TypeSerializer
# from .models import Type, Question

# Create your views here.

# class QuestionViewSet(mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.ListModelMixin,
#                       viewsets.GenericViewSet):
#
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = (IsAdminOrReadOnly, )
#
#     # def create(self, request, *args, **kwargs):
#     #     return super().create(request, *args, **kwargs)
#
#
# class TypeViewSet(mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.ListModelMixin,
#                   mixins.UpdateModelMixin,
#                   viewsets.GenericViewSet):
#     queryset = Type.objects.all()
#     serializer_class = TypeSerializer
#     permission_classes = (IsAdminOrReadOnly, )
