from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from statistic.models import Statistic, StatisticsAnswers
from statistic.serializers import StatisticSerializer, StatisticsAnswersSerializer



class StatisticViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer

    filterset_fields = '__all__'


class StatisticsAnswersViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = StatisticsAnswers.objects.all()
    serializer_class = StatisticsAnswersSerializer

    filterset_fields = ['statistic__test__id', 'statistic__student__id']
