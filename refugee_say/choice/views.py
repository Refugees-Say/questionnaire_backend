from rest_framework import viewsets

from refugee_say.contrib.permissions import IsAdminOrReadOnly

from .models import Choice
from .serializers import ChoiceSerializer


class ChoiceViewSet(viewsets.ModelViewSet):

    model = Choice
    queryset = Choice.objects.all()

    permission_classes = (IsAdminOrReadOnly, )
    serializer_class = ChoiceSerializer


# class TypeViewSet(viewsets.ModelViewSet):
#
#     model = Type
#     queryset = Type.objects.all()
#
#     permission_classes = (IsAdminOrReadOnly, )
#     serializer_class = TypeSerializer
