from django.db.models.query import QuerySet

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

    def list(self, request):
        question_ids_param = request.query_params.get('question_id')  # Получаем параметр question_id из запроса
        question_ids = question_ids_param.split(',') if ',' in question_ids_param else [question_ids_param]

        all_answers = {}
        for question_id in question_ids:
            answers = Answer.objects.filter(question_id=question_id)
            serialized_answers = self.serializer_class(answers, many=True).data
            all_answers[question_id] = serialized_answers

        return Response(all_answers)


class GetAnswerByQuestionIdViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    lookup_field = 'question'
    lookup_url_kwarg = 'pk'

    def list(self, request, pk=None, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(pk=pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, pk=None):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.filter(question__pk=pk)
        return queryset

class GetAnswerByQuestionsIdViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = QuestionsGroupSerializer

    def list(self, request, *args, **kwargs):
        questions_base_id = self.kwargs.get('pk')
        response_mode = request.query_params.get('mode')

        questions_base = QuestionsBase.objects.get(id=questions_base_id)

        questions_base_serializer = QuestionsBaseSerializer(questions_base).data

        if response_mode == '0':
            return Response({'questions_base': questions_base_serializer})
        else:
            # Получаем все QuestionsGroup, принадлежащие QuestionsBase
            questions_groups = QuestionsGroup.objects.filter(questions_base=questions_base)
            serialized_data = []

            # Перебираем каждый QuestionsGroup и добавляем вложенные question и answers
            for group in questions_groups:
                serialized_group = self.get_serializer(group).data
                questions = Question.objects.filter(questions_group=group)
                serialized_questions = QuestionSerializer(questions, many=True).data

                # Добавляем в каждый вопрос все связанные ответы
                for question_data in serialized_questions:
                    answers = Answer.objects.filter(question=question_data['id'])
                    question_data['answers'] = AnswerSerializer(answers, many=True).data

                serialized_group['questions'] = serialized_questions
                serialized_data.append(serialized_group)

            response_data = {
                'questions_base': questions_base_serializer,
                'questions_groups': serialized_data,
            }

            return Response(response_data)
