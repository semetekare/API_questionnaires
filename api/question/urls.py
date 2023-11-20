from django.urls import path, include

from rest_framework import routers

from question.views import TestViewSet, AnswerViewSet, QuestionViewSet, QuestionsBaseViewSet, QuestionsGroupViewSet, TestsQuestionsGroupsViewSet


router = routers.SimpleRouter()
router.register(r'test', TestViewSet)
router.register(r'asnwer', AnswerViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'questionsBase', QuestionsBaseViewSet)
router.register(r'questionsGroup', QuestionsGroupViewSet)
router.register(r'testsQuestionsGroups', TestsQuestionsGroupsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
