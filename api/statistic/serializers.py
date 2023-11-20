from rest_framework import serializers

from statistic.models import Statistic, StatisticsAnswers



class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'


class StatisticsAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticsAnswers
        fields = '__all__'
