# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_ortoloco', '0018_auto_20161102_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abo',
            name='extra_abos',
        ),
        migrations.RemoveField(
            model_name='abo',
            name='future_extra_abos',
        ),
    ]
