from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from .models import Profile, School, Teacher, Classform, Student, Task, Subject, Parent


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class ProfileAdminForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ['notes']
    #readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Profile, ProfileAdmin)


class SchoolAdminForm(forms.ModelForm):

    class Meta:
        model = School
        fields = '__all__'


class SchoolAdmin(admin.ModelAdmin):
    form = SchoolAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'email', 'phone', 'contactName']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(School, SchoolAdmin)


class TeacherAdminForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdmin(admin.ModelAdmin):
    form = TeacherAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'email', 'roles']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Teacher, TeacherAdmin)


class ClassformAdminForm(forms.ModelForm):

    class Meta:
        model = Classform
        fields = '__all__'


class ClassformAdmin(admin.ModelAdmin):
    form = ClassformAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Classform, ClassformAdmin)


class StudentAdminForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Student, StudentAdmin)


class TaskAdminForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'type', 'graded', 'grade', 'comment', 'image', 'document']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Task, TaskAdmin)


class SubjectAdminForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Subject, SubjectAdmin)


class ParentAdminForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = '__all__'


class ParentAdmin(admin.ModelAdmin):
    form = ParentAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'parentID', 'email', 'phone', 'verified']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Parent, ParentAdmin)


