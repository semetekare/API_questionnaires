from django.urls import path, include

from rest_framework import routers

from user.views import CustomUserViewSet, AdminViewSet, TeacherViewSet, UniversityViewSet


router = routers.SimpleRouter()
router.register(r'user', CustomUserViewSet)
router.register(r'admin', AdminViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'university', UniversityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
