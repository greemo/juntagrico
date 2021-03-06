# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juntagrico', '0005_subscription_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailtemplate',
            options={'permissions': (('can_load_templates', 'Benutzer kann Templates laden'),), 'verbose_name': 'MailTemplate', 'verbose_name_plural': 'MailTemplates'},
        ),
        migrations.AddField(
            model_name='extrasubbillingperiod',
            name='cancel_day',
            field=models.PositiveIntegerField(default=1, verbose_name='Kündigungs Tag'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extrasubbillingperiod',
            name='cancel_month',
            field=models.PositiveIntegerField(choices=[(1, 'Januar'), (2, 'Februar'), (3, 'März'), (4, 'April'), (5, 'Mai'), (6, 'Juni'), (7, 'Juli'), (8, 'August'), (9, 'September'), (10, 'Oktober'), (11, 'November'), (12, 'Dezember')], default=1, verbose_name='Kündigungs Monat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='cancelation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Kündigüngssdatum'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='canceled',
            field=models.BooleanField(default=False, verbose_name='gekündigt'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Gewünschtes Enddatum'),
        ),
        migrations.AlterField(
            model_name='extrasubbillingperiod',
            name='code',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='Code für Teilabrechnung'),
        ),
    ]
