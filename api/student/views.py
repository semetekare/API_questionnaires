from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from student.models import Subject, Student, StudentsGroup, StudentsGroupsSubjects, StudentsGroupsStudents
from student.serializers import SubjectSerializer, StudentSerializer, StudentsGroupSerializer, StudentsGroupsSubjectsSerializer, StudentsGroupsStudentsSerializer
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

    # @api_view(['GET'])
    # def get_students_by_group_id(request, students_group_id):
    #     try:
    #         # Находим всех студентов по students_group_id
    #         students_group_students = StudentsGroupsStudents.objects.filter(students_group_id=students_group_id)
    #
    #         # Получаем идентификаторы студентов
    #         student_ids = students_group_students.values_list('student_id', flat=True)
    #
    #         # Получаем информацию о студентах по найденным идентификаторам
    #         students = Student.objects.filter(id__in=student_ids)
    #
    #         # Сериализуем полученных студентов
    #         serializer = StudentSerializer(students, many=True)
    #
    #         return Response(serializer.data)
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=500)
