from rest_framework import viewsets

from refugee_say.contrib.permissions import IsAdminOrReadOnly
from .models import Questionnaire, QuestionOrder
from .serializers import QuestionnaireSerializer, QuestionOrderSerializer


class QuestionnaireViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly, )
    serializer_class =  QuestionnaireSerializer
    queryset = Questionnaire.objects.all()


class QuestionOrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly, )
    serializer_class = QuestionOrderSerializer
    queryset = QuestionOrder.objects.all()
