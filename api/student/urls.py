from django.urls import path, include

from rest_framework import routers

from student.views import SubjectViewSet, StudentViewSet, StudentsGroupViewSet, StudentsGroupsStudentsViewSet, StudentsGroupsSubjectsViewSet


router = routers.SimpleRouter()
router.register(r'subject', SubjectViewSet)
router.register(r'student', StudentViewSet)
router.register(r'studentsGroup', StudentsGroupViewSet)
router.register(r'studentsGroupsStudents', StudentsGroupsStudentsViewSet)
router.register(r'studentsGroupsSubjects', StudentsGroupsSubjectsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('create_subject/', SubjectViewSet.as_view({'post': 'create'}), name='subject-create'),
]
