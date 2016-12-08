# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-11-14 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('my_ortoloco', '0020_auto_20161104_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False, verbose_name=b'bezahlt')),
                ('bill_date', models.DateField(blank=True, null=True, verbose_name=b'Aktivierungssdatum')),
                ('ref_number', models.CharField(max_length=30, unique=True, verbose_name=b'Referenznummer')),
                ('amount', models.FloatField(verbose_name=b'Betrag')),
            ],
            options={
                'verbose_name': 'Rechnung',
                'verbose_name_plural': 'Rechnungen',
            },
        ),
        migrations.CreateModel(
            name='Billable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_my_ortoloco.billable_set+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Verrechenbare Einheit',
                'verbose_name_plural': 'Verrechenbare Einhaiten',
            },
        ),
        migrations.RenameField(
            model_name='extraabo',
            old_name='abo',
            new_name='main_abo',
        ),
        migrations.AddField(
            model_name='bill',
            name='billable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bills', to='my_ortoloco.Billable'),
        ),
        migrations.AddField(
            model_name='abo',
            name='billable_ptr',
            field=models.IntegerField(null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anteilschein',
            name='billable_ptr',
            field=models.IntegerField(null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraabo',
            name='billable_ptr',
            field=models.IntegerField(null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loco',
            name='tmp_abo_id',
            field=models.IntegerField(null=True),
            preserve_default=False,
        ),
        
        migrations.AddField(
            model_name='extraabo',
            name='tmp_abo_id',
            field=models.IntegerField(null=True),
            preserve_default=False,
        ),
    ]
