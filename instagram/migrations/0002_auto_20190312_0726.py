# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-12 04:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
    ]
