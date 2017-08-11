from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response

from refugee_say.contrib.permissions import IsAdminOrReadOnly
from .models import Questionnaire, QuestionOrder
from .serializers import QuestionnaireSerializer, QuestionOrderSerializer

from .serializers import QuestionnaireSerializerV2

class QuestionnaireViewSet__(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAdminOrReadOnly, )
    serializer_class =  QuestionnaireSerializerV2
    queryset = Questionnaire.objects.all()


class QuestionnaireViewSet(viewsets.ViewSet):
    queryset = Questionnaire.objects.all()
    def get_queryset(self):
        return self.queryset


    def list(self, request):
        qs = self.get_queryset()
        l = set()
        for q in qs:
            q.questions = QuestionOrder.objects.filter(questionnaire=q).order_by('order')
            l.add(q)
        return Response(QuestionnaireSerializer(l, many=True).data)



    # queryset = Questionnaire.objects.all()
    # # serializer_class = QuestionnaireSerializer
    #
    # def get_serializer(self, *args, **kwargs):
    #     print(args)
    #     print(kwargs)
    #     items = []
    #     for questionnaire in args[0]:
    #         questionnaire.questions = []
    #             # JSONRenderer().render(QuestionOrderSerializer(
    #             # QuestionOrder.objects.filter(questionnaire=questionnaire).order_by('order'), many=True).is_valid().data)
    #         print(questionnaire.questions)
    #         items.append(questionnaire)
    #     return super().get_serializer(items, *args, **kwargs)
    #
    # def get_serializer_class(self):
    #     return QuestionnaireSerializer


class QuestionOrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly, )
    serializer_class = QuestionOrderSerializer
    queryset = QuestionOrder.objects.all()
