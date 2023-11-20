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


class StatisticsAnswersViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = StatisticsAnswers.objects.all()
    serializer_class = StatisticsAnswersSerializer
