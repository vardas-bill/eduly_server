from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'school', api.SchoolViewSet)
router.register(r'teacher', api.TeacherViewSet)
router.register(r'classform', api.ClassformViewSet)
router.register(r'student', api.StudentViewSet)
router.register(r'task', api.TaskViewSet)
router.register(r'subject', api.SubjectViewSet)
router.register(r'parent', api.ParentViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for School
    url(r'^eduly/school/$', views.SchoolListView.as_view(), name='eduly_school_list'),
    url(r'^eduly/school/create/$', views.SchoolCreateView.as_view(), name='eduly_school_create'),
    url(r'^eduly/school/detail/(?P<slug>\S+)/$', views.SchoolDetailView.as_view(), name='eduly_school_detail'),
    url(r'^eduly/school/update/(?P<slug>\S+)/$', views.SchoolUpdateView.as_view(), name='eduly_school_update'),
)

urlpatterns += (
    # urls for Teacher
    url(r'^eduly/teacher/$', views.TeacherListView.as_view(), name='eduly_teacher_list'),
    url(r'^eduly/teacher/create/$', views.TeacherCreateView.as_view(), name='eduly_teacher_create'),
    url(r'^eduly/teacher/detail/(?P<slug>\S+)/$', views.TeacherDetailView.as_view(), name='eduly_teacher_detail'),
    url(r'^eduly/teacher/update/(?P<slug>\S+)/$', views.TeacherUpdateView.as_view(), name='eduly_teacher_update'),
)

urlpatterns += (
    # urls for Classform
    url(r'^eduly/classform/$', views.ClassformListView.as_view(), name='eduly_classform_list'),
    url(r'^eduly/classform/create/$', views.ClassformCreateView.as_view(), name='eduly_classform_create'),
    url(r'^eduly/classform/detail/(?P<slug>\S+)/$', views.ClassformDetailView.as_view(), name='eduly_classform_detail'),
    url(r'^eduly/classform/update/(?P<slug>\S+)/$', views.ClassformUpdateView.as_view(), name='eduly_classform_update'),
)

urlpatterns += (
    # urls for Student
    url(r'^eduly/student/$', views.StudentListView.as_view(), name='eduly_student_list'),
    url(r'^eduly/student/create/$', views.StudentCreateView.as_view(), name='eduly_student_create'),
    url(r'^eduly/student/detail/(?P<slug>\S+)/$', views.StudentDetailView.as_view(), name='eduly_student_detail'),
    url(r'^eduly/student/update/(?P<slug>\S+)/$', views.StudentUpdateView.as_view(), name='eduly_student_update'),
)

urlpatterns += (
    # urls for Task
    url(r'^eduly/task/$', views.TaskListView.as_view(), name='eduly_task_list'),
    url(r'^eduly/task/create/$', views.TaskCreateView.as_view(), name='eduly_task_create'),
    url(r'^eduly/task/detail/(?P<slug>\S+)/$', views.TaskDetailView.as_view(), name='eduly_task_detail'),
    url(r'^eduly/task/update/(?P<slug>\S+)/$', views.TaskUpdateView.as_view(), name='eduly_task_update'),
)

urlpatterns += (
    # urls for Subject
    url(r'^eduly/subject/$', views.SubjectListView.as_view(), name='eduly_subject_list'),
    url(r'^eduly/subject/create/$', views.SubjectCreateView.as_view(), name='eduly_subject_create'),
    url(r'^eduly/subject/detail/(?P<slug>\S+)/$', views.SubjectDetailView.as_view(), name='eduly_subject_detail'),
    url(r'^eduly/subject/update/(?P<slug>\S+)/$', views.SubjectUpdateView.as_view(), name='eduly_subject_update'),
)

urlpatterns += (
    # urls for Parent
    url(r'^eduly/parent/$', views.ParentListView.as_view(), name='eduly_parent_list'),
    url(r'^eduly/parent/create/$', views.ParentCreateView.as_view(), name='eduly_parent_create'),
    url(r'^eduly/parent/detail/(?P<slug>\S+)/$', views.ParentDetailView.as_view(), name='eduly_parent_detail'),
    url(r'^eduly/parent/update/(?P<slug>\S+)/$', views.ParentUpdateView.as_view(), name='eduly_parent_update'),
)

