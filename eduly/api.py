from . import models
from . import serializers
from rest_framework import viewsets, permissions


class SchoolViewSet(viewsets.ModelViewSet):
    """ViewSet for the School class"""

    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    """ViewSet for the Teacher class"""

    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClassformViewSet(viewsets.ModelViewSet):
    """ViewSet for the Classform class"""

    queryset = models.Classform.objects.all()
    serializer_class = serializers.ClassformSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Student class"""

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for the Task class"""

    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Parent class"""

    queryset = models.Parent.objects.all()
    serializer_class = serializers.ParentSerializer
    permission_classes = [permissions.IsAuthenticated]


