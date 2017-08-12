from rest_framework import viewsets

from refugee_say.contrib.permissions import IsOwner
from .models import Response
from .serializers import ResponseSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwner, )
    serializer_class = ResponseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return Response.objects.all()
        return Response.objects.filter(user=self.request.user)
