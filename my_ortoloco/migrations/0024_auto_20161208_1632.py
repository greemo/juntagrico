# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-08 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_ortoloco', '0023_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='anteilschein',
            name='id',
        ),
        migrations.RemoveField(
            model_name='extraabo',
            name='id',
        ),
        migrations.AlterField(
            model_name='abo',
            name='billable_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_ortoloco.Billable'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anteilschein',
            name='billable_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_ortoloco.Billable'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extraabo',
            name='billable_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_ortoloco.Billable'),
            preserve_default=False,
        ),
    ]
