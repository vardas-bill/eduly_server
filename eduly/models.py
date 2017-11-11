from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# User profile info
class Profile(models.Model):

    # Relationship Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey('eduly.School', default=1)

    notes = models.TextField(max_length=500, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class School(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=500, blank=True)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    contactName = models.CharField(max_length=30)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('eduly_school_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('eduly_school_update', args=(self.slug,))


class Teacher(models.Model):

    SCHOOL_ADMIN = 0
    CLASS_ADMIN = 1
    TASK_ADMIN = 2

    ROLES = {
        (SCHOOL_ADMIN, "School administrator"),
        (CLASS_ADMIN, "Class administrator"),
        (TASK_ADMIN, "Task administrator")
    }

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    email = models.CharField(max_length=30)
    roles = models.IntegerField("Role", choices=ROLES, default=1)

    # Relationship Fields
    school = models.ForeignKey('eduly.School', )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('eduly_teacher_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('eduly_teacher_update', args=(self.slug,))


class Classform(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    school = models.ForeignKey('eduly.School', )
    teachers = models.ManyToManyField('eduly.Teacher', )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('eduly_classform_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('eduly_classform_update', args=(self.slug,))


class Student(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    school = models.ForeignKey('eduly.School', )
    classform = models.ForeignKey('eduly.Classform', )
    tasks = models.ManyToManyField('eduly.Task', )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('eduly_student_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('eduly_student_update', args=(self.slug,))


class Task(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.CharField(max_length=30)
    graded = models.BooleanField()
    grade = models.CharField(max_length=15)
    comment = models.TextField(max_length=100)
    image = models.ImageField(upload_to="upload/images/")
    document = models.FileField(upload_to="upload/files/")

    # Relationship Fields
    subject = models.ForeignKey('eduly.Subject', )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('eduly_task_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('eduly_task_update', args=(self.slug,))


class Subject(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('eduly_subject_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('eduly_subject_update', args=(self.slug,))


class Parent(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    parentID = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    verified = models.BooleanField()

    # Relationship Fields
    children = models.ManyToManyField('eduly.Student', )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('eduly_parent_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('eduly_parent_update', args=(self.slug,))


