from rest_framework import viewsets

from refugee_say.contrib.permissions import IsAdminOrReadOnly
from .models import RadioQuestion
from .serializers import RadioQuestionSerializer

class RadioQuestionViewSet(viewsets.ModelViewSet):

    model = RadioQuestion

    queryset = RadioQuestion.objects.all()
    serializer_class = RadioQuestionSerializer
    permission_classes = (IsAdminOrReadOnly, )
