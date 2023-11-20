from django.urls import path, include

from rest_framework import routers

from statistic.views import StatisticViewSet, StatisticsAnswersViewSet


router = routers.SimpleRouter()
router.register(r'statistic', StatisticViewSet)
router.register(r'statisticAnswers', StatisticsAnswersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
