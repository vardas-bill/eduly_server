from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import School, Teacher, Classform, Student, Task, Subject, Parent
from .forms import SchoolForm, TeacherForm, ClassformForm, StudentForm, TaskForm, SubjectForm, ParentForm

@method_decorator(login_required, name='dispatch')
class SchoolListView(ListView):
    model = School


@method_decorator(login_required, name='dispatch')
class SchoolCreateView(CreateView):
    model = School
    form_class = SchoolForm


@method_decorator(login_required, name='dispatch')
class SchoolDetailView(DetailView):
    model = School


@method_decorator(login_required, name='dispatch')
class SchoolUpdateView(UpdateView):
    model = School
    form_class = SchoolForm


@method_decorator(login_required, name='dispatch')
class TeacherListView(ListView):
    model = Teacher

    def get_queryset(self):
        return Teacher.objects.filter(school=self.request.user.profile.school)


@method_decorator(login_required, name='dispatch')
class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm

    def form_valid(self, form):
        form.instance.school = self.request.user.profile.school
        return super(TeacherCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TeacherDetailView(DetailView):
    model = Teacher


@method_decorator(login_required, name='dispatch')
class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm


@method_decorator(login_required, name='dispatch')
class ClassformListView(ListView):
    model = Classform


@method_decorator(login_required, name='dispatch')
class ClassformCreateView(CreateView):
    model = Classform
    form_class = ClassformForm


@method_decorator(login_required, name='dispatch')
class ClassformDetailView(DetailView):
    model = Classform


@method_decorator(login_required, name='dispatch')
class ClassformUpdateView(UpdateView):
    model = Classform
    form_class = ClassformForm


@method_decorator(login_required, name='dispatch')
class StudentListView(ListView):
    model = Student


@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm


@method_decorator(login_required, name='dispatch')
class StudentDetailView(DetailView):
    model = Student


@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm


@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task


@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm


@method_decorator(login_required, name='dispatch')
class TaskDetailView(DetailView):
    model = Task


@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm


@method_decorator(login_required, name='dispatch')
class SubjectListView(ListView):
    model = Subject


@method_decorator(login_required, name='dispatch')
class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm


@method_decorator(login_required, name='dispatch')
class SubjectDetailView(DetailView):
    model = Subject


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm


class ParentListView(ListView):
    model = Parent


class ParentCreateView(CreateView):
    model = Parent
    form_class = ParentForm


class ParentDetailView(DetailView):
    model = Parent


class ParentUpdateView(UpdateView):
    model = Parent
    form_class = ParentForm

