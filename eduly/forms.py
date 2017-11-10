from django import forms
from .models import Profile, School, Teacher, Classform, Student, Task, Subject, Parent


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('school', 'notes')


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'email', 'phone', 'contactName']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'roles']#, 'school']


class ClassformForm(forms.ModelForm):
    class Meta:
        model = Classform
        fields = ['name', 'school', 'teachers']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'school', 'classform', 'tasks']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'type', 'graded', 'grade', 'comment', 'image', 'document', 'subject']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name', 'parentID', 'email', 'phone', 'verified', 'children']


