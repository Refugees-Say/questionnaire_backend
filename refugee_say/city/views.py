from rest_framework import viewsets

from refugee_say.contrib.permissions import IsAdminOrReadOnly
from .models import City
from .serializers import CitySerializer

class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = CitySerializer
