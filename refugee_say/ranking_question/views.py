from rest_framework import viewsets

from refugee_say.contrib.permissions import IsAdminOrReadOnly

from .models import RankingQuestion
from .serializers import RankingQuestionSerializer

class RankingQuestionViewSet(viewsets.ModelViewSet):

    model = RankingQuestion
    queryset = RankingQuestion.objects.all()

    serializer_class = RankingQuestionSerializer
    permission_classes = (IsAdminOrReadOnly, )
