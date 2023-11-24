from django.urls import path, include

from rest_framework import routers

from question.views import TestViewSet, AnswerViewSet, QuestionViewSet, QuestionsBaseViewSet, QuestionsGroupViewSet, \
    TestsQuestionsGroupsViewSet, \
    GetAnswerByQuestionIdViewSet, GetAnswerByQuestionsIdViewSet

router = routers.SimpleRouter()
router.register(r'test', TestViewSet)
router.register(r'answer', AnswerViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'questionsBase', QuestionsBaseViewSet)
router.register(r'questionsGroup', QuestionsGroupViewSet)
router.register(r'testsQuestionsGroups', TestsQuestionsGroupsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questionsbase/<int:pk>/', GetAnswerByQuestionsIdViewSet.as_view({'get': 'list'}))
]
