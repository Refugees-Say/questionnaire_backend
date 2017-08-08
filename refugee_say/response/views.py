from rest_framework import viewsets, permissions

from refugee_say.contrib.permissions import IsOwner
from .models import Response
from .serializers import ResponseSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    permission_classes = (IsOwner, )
    serializer_class = ResponseSerializer
    model = Response

    def create(self, request, *args, **kwargs):
        self.permission_classes = (permissions.AllowAny, )
        return super().create(request, *args, **kwargs)
