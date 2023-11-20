from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from student.models import Subject, Student, StudentsGroup, StudentsGroupsSubjects, StudentsGroupsStudents
from student.serializers import SubjectSerializer, StudentSerializer, StudentsGroupSerializer, StudentsGroupsSubjectsSerializer, StudentsGroupsStudentsSerializer 



class SubjectViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentsGroupViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = StudentsGroup.objects.all()
    serializer_class = StudentsGroupSerializer


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
