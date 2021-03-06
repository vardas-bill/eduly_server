# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eduly', '0002_auto_20171109_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='address',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='roles',
            field=models.IntegerField(choices=[(2, 'Task administrator'), (0, 'School administrator'), (1, 'Class administrator')], default=1, verbose_name='Role'),
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduly.School'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
