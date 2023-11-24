from django.urls import path, include

from rest_framework import routers

from student.views import SubjectViewSet, StudentViewSet, StudentsGroupViewSet, StudentsGroupsStudentsViewSet, \
    StudentsGroupsSubjectsViewSet, GetStudentsByStudentsGroupIdViewSet


router = routers.SimpleRouter()
router.register(r'subject', SubjectViewSet)
router.register(r'student', StudentViewSet)
router.register(r'studentsGroup', StudentsGroupViewSet)
router.register(r'studentsGroupsStudents', StudentsGroupsStudentsViewSet)
router.register(r'studentsGroupsSubjects', StudentsGroupsSubjectsViewSet)
# router.register(r'testCustom', GetStudentsByStudentsGroupIdViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('students/studentsGroup/<int:pk>/', GetStudentsByStudentsGroupIdViewSet.as_view({'get': 'list'})),
    #path('create_subject/', SubjectViewSet.as_view({'post': 'create'}), name='subject-create'),
]
