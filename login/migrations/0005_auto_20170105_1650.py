# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_task_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='published_date',
            new_name='due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='text',
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(default='middle', max_length=50),
        ),
    ]