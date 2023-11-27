from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from user.models import CustomUser, Admin, Teacher, University
from user.serializers import CustomUserSerializer, AdminSerializer, TeacherSerializer, UniversitySerializer



class CustomUserViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class AdminViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class TeacherViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class UniversityViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
