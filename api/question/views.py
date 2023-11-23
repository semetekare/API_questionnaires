from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
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

    def by_subject(self, request, *args, **kwargs):
        subject_id = request.query_params.get('subject_id')
        if not subject_id:
            return Response({'error': 'Please provide subject_id'}, status=400)

        questions_base = QuestionsBase.objects.filter(subject__id=subject_id)
        serializer = self.get_serializer(questions_base, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def clone(self, request, pk=None):
        original_question_base = self.get_object()
        cloned_data = {
            'subject': original_question_base.subject.id,
            'title': f"{original_question_base.title}"
        }

        serializer = self.get_serializer(data=cloned_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=201)

class QuestionsGroupViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = QuestionsGroup.objects.all()
    serializer_class = QuestionsGroupSerializer

    @action(detail=True, methods=['post'])
    def clone(self, request, pk=None):
        original_questions_group = self.get_object()
        cloned_data = {
            'questions_base': original_questions_group.questions_base.id,
            'title': f"{original_questions_group.title}"
        }

        serializer = self.get_serializer(data=cloned_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=201)


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
