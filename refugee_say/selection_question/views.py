from rest_framework import viewsets

from refugee_say.contrib.permissions import IsAdminOrReadOnly

from .models import SelectionQuestion
from .serializers import SelectionQuestionSerializer


class SelectionQuestionViewSet(viewsets.ModelViewSet):

    model = SelectionQuestion
    queryset = SelectionQuestion.objects.all()

    permission_classes = (IsAdminOrReadOnly, )
    serializer_class = SelectionQuestionSerializer
