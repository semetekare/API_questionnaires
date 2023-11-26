from django.db.models.query import QuerySet

from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from student.models import Subject, Student, StudentsGroup, StudentsGroupsSubjects, StudentsGroupsStudents
from student.serializers import SubjectSerializer, StudentSerializer, StudentsGroupSerializer, StudentsGroupsSubjectsSerializer, \
    StudentsGroupsStudentsSerializer, GetStudentsByStudentsGroupIdSerializer, CheckStudentSerializer
from user.models import University


class SubjectViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def by_university(self, request, *args, **kwargs):
        university_id = request.query_params.get('university_id')
        if not university_id:
            return Response({'error': 'Please provide university_id'}, status=400)

        subjects = Subject.objects.filter(university__id=university_id)
        serializer = self.get_serializer(subjects, many=True)
        return Response(serializer.data)

class StudentViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CheckStudentViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = CheckStudentSerializer

    lookup_field = 'tg_username'


class StudentsGroupViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = StudentsGroup.objects.all()
    serializer_class = StudentsGroupSerializer

    def list(self, request):
        subject_id = request.query_params.get('subject_id')
        if not subject_id:
            return Response({'error': 'Please provide subject_id'}, status=400)

        # Получаем университеты, связанные с указанным subject_id
        universities = University.objects.filter(subject__id=subject_id)

        # Получаем все students_group для этих университетов
        students_groups = StudentsGroup.objects.filter(university__in=universities)

        serializer = self.get_serializer(students_groups, many=True)
        return Response(serializer.data)


class StudentsGroupsSubjectsViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = StudentsGroupsSubjects.objects.all()
    serializer_class = StudentsGroupsSubjectsSerializer


class StudentsGroupsStudentsViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = StudentsGroupsStudents.objects.all()
    serializer_class = StudentsGroupsStudentsSerializer


class GetStudentsByStudentsGroupIdViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = StudentsGroupsStudents.objects.all()
    serializer_class = GetStudentsByStudentsGroupIdSerializer

    lookup_field = 'students_group'
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
            queryset = queryset.filter(students_group__pk=pk)
        return queryset