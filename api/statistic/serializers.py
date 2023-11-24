from rest_framework import serializers

from statistic.models import Statistic, StatisticsAnswers
from question.serializers import AnswerSerializer



class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'


class StatisticsAnswersSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(source='question.id')

    class Meta:
        model = StatisticsAnswers
        fields = '__all__'
        depth = 3
