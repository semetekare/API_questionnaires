from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from question.models import Test, TestsQuestionsGroups, QuestionsBase, QuestionsGroup, Question, Answer
from question.serializers import TestSerializer, TestsQuestionsGroupsSerializer, QuestionsBaseSerializer, QuestionsGroupSerializer, QuestionSerializer, AnswerSerializer



class TestViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestsQuestionsGroupsViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = TestsQuestionsGroups.objects.all()
    serializer_class = TestsQuestionsGroupsSerializer


class QuestionsBaseViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = QuestionsBase.objects.all()
    serializer_class = QuestionsBaseSerializer


class QuestionsGroupViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = QuestionsGroup.objects.all()
    serializer_class = QuestionsGroupSerializer


class QuestionViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
