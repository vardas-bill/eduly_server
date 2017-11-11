import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import School, Teacher, Classform, Student, Task, Subject, Parent
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_school(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["email"] = "email"
    defaults["phone"] = "phone"
    defaults["contactName"] = "contactName"
    defaults.update(**kwargs)
    return School.objects.create(**defaults)


def create_teacher(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["email"] = "email"
    defaults["roles"] = "roles"
    defaults.update(**kwargs)
    if "school" not in defaults:
        defaults["school"] = create_school()
    return Teacher.objects.create(**defaults)


def create_classform(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "school" not in defaults:
        defaults["school"] = create_school()
    if "teachers" not in defaults:
        defaults["teachers"] = create_teacher()
    return Classform.objects.create(**defaults)


def create_student(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "school" not in defaults:
        defaults["school"] = create_school()
    if "classform" not in defaults:
        defaults["classform"] = create_classform()
    if "tasks" not in defaults:
        defaults["tasks"] = create_task()
    return Student.objects.create(**defaults)


def create_task(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["type"] = "type"
    defaults["graded"] = "graded"
    defaults["grade"] = "grade"
    defaults["comment"] = "comment"
    defaults["image"] = "image"
    defaults["document"] = "document"
    defaults.update(**kwargs)
    if "subject" not in defaults:
        defaults["subject"] = create_subject()
    return Task.objects.create(**defaults)


def create_subject(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Subject.objects.create(**defaults)


def create_parent(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["parentID"] = "parentID"
    defaults["email"] = "email"
    defaults["phone"] = "phone"
    defaults["verified"] = "verified"
    defaults.update(**kwargs)
    if "children" not in defaults:
        defaults["children"] = create_student()
    return Parent.objects.create(**defaults)


class SchoolViewTest(unittest.TestCase):
    '''
    Tests for School
    '''
    def setUp(self):
        self.client = Client()

    def test_list_school(self):
        url = reverse('eduly_school_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_school(self):
        url = reverse('eduly_school_create')
        data = {
            "name": "name",
            "email": "email",
            "phone": "phone",
            "contactName": "contactName",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_school(self):
        school = create_school()
        url = reverse('eduly_school_detail', args=[school.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_school(self):
        school = create_school()
        data = {
            "name": "name",
            "email": "email",
            "phone": "phone",
            "contactName": "contactName",
        }
        url = reverse('eduly_school_update', args=[school.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TeacherViewTest(unittest.TestCase):
    '''
    Tests for Teacher
    '''
    def setUp(self):
        self.client = Client()

    def test_list_teacher(self):
        url = reverse('eduly_teacher_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_teacher(self):
        url = reverse('eduly_teacher_create')
        data = {
            "name": "name",
            "email": "email",
            "roles": "roles",
            "school": create_school().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_teacher(self):
        teacher = create_teacher()
        url = reverse('eduly_teacher_detail', args=[teacher.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_teacher(self):
        teacher = create_teacher()
        data = {
            "name": "name",
            "email": "email",
            "roles": "roles",
            "school": create_school().pk,
        }
        url = reverse('eduly_teacher_update', args=[teacher.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ClassformViewTest(unittest.TestCase):
    '''
    Tests for Classform
    '''
    def setUp(self):
        self.client = Client()

    def test_list_classform(self):
        url = reverse('eduly_classform_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_classform(self):
        url = reverse('eduly_classform_create')
        data = {
            "name": "name",
            "school": create_school().pk,
            "teachers": create_teacher().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_classform(self):
        classform = create_classform()
        url = reverse('eduly_classform_detail', args=[classform.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_classform(self):
        classform = create_classform()
        data = {
            "name": "name",
            "school": create_school().pk,
            "teachers": create_teacher().pk,
        }
        url = reverse('eduly_classform_update', args=[classform.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class StudentViewTest(unittest.TestCase):
    '''
    Tests for Student
    '''
    def setUp(self):
        self.client = Client()

    def test_list_student(self):
        url = reverse('eduly_student_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_student(self):
        url = reverse('eduly_student_create')
        data = {
            "name": "name",
            "school": create_school().pk,
            "classform": create_classform().pk,
            "tasks": create_task().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_student(self):
        student = create_student()
        url = reverse('eduly_student_detail', args=[student.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_student(self):
        student = create_student()
        data = {
            "name": "name",
            "school": create_school().pk,
            "classform": create_classform().pk,
            "tasks": create_task().pk,
        }
        url = reverse('eduly_student_update', args=[student.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TaskViewTest(unittest.TestCase):
    '''
    Tests for Task
    '''
    def setUp(self):
        self.client = Client()

    def test_list_task(self):
        url = reverse('eduly_task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        url = reverse('eduly_task_create')
        data = {
            "name": "name",
            "type": "type",
            "graded": "graded",
            "grade": "grade",
            "comment": "comment",
            "image": "image",
            "document": "document",
            "subject": create_subject().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_task(self):
        task = create_task()
        url = reverse('eduly_task_detail', args=[task.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        task = create_task()
        data = {
            "name": "name",
            "type": "type",
            "graded": "graded",
            "grade": "grade",
            "comment": "comment",
            "image": "image",
            "document": "document",
            "subject": create_subject().pk,
        }
        url = reverse('eduly_task_update', args=[task.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SubjectViewTest(unittest.TestCase):
    '''
    Tests for Subject
    '''
    def setUp(self):
        self.client = Client()

    def test_list_subject(self):
        url = reverse('eduly_subject_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_subject(self):
        url = reverse('eduly_subject_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_subject(self):
        subject = create_subject()
        url = reverse('eduly_subject_detail', args=[subject.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_subject(self):
        subject = create_subject()
        data = {
            "name": "name",
        }
        url = reverse('eduly_subject_update', args=[subject.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ParentViewTest(unittest.TestCase):
    '''
    Tests for Parent
    '''
    def setUp(self):
        self.client = Client()

    def test_list_parent(self):
        url = reverse('eduly_parent_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_parent(self):
        url = reverse('eduly_parent_create')
        data = {
            "name": "name",
            "parentID": "parentID",
            "email": "email",
            "phone": "phone",
            "verified": "verified",
            "children": create_student().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_parent(self):
        parent = create_parent()
        url = reverse('eduly_parent_detail', args=[parent.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_parent(self):
        parent = create_parent()
        data = {
            "name": "name",
            "parentID": "parentID",
            "email": "email",
            "phone": "phone",
            "verified": "verified",
            "children": create_student().pk,
        }
        url = reverse('eduly_parent_update', args=[parent.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


