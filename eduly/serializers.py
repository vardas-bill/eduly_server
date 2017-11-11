from . import models

from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.School
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'email', 
            'phone', 
            'contactName', 
        )


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Teacher
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'email', 
            'roles', 
        )


class ClassformSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Classform
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'type', 
            'graded', 
            'grade', 
            'comment', 
            'image', 
            'document', 
        )


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subject
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Parent
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'parentID', 
            'email', 
            'phone', 
            'verified', 
        )


