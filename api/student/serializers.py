from rest_framework import serializers

from student.models import Subject, Student, StudentsGroup, StudentsGroupsSubjects, StudentsGroupsStudents



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


class StudentsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsGroup
        fields = '__all__'


class StudentsGroupsSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsGroupsSubjects
        fields = '__all__'


class StudentsGroupsStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsGroupsStudents
        fields = '__all__'

class GetStudentsByStudentsGroupIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsGroupsStudents
        fields = ['student']
        depth = 1