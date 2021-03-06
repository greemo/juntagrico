# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juntagrico', '0007_auto_20171222_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(verbose_name='Lieferdatum')),
                ('subscription_size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='juntagrico.SubscriptionSize', verbose_name='Abo-Grösse')),
            ],
            options={
                'verbose_name': 'Lieferung',
                'verbose_name_plural': 'Lieferungen',
            },
        ),
        migrations.CreateModel(
            name='DeliveryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Name')),
                ('amount', models.CharField(default='', max_length=100, verbose_name='Menge')),
                ('comment', models.CharField(blank=True, default='', max_length=1000, verbose_name='Kommentar')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='juntagrico.Delivery', verbose_name='Lieferung')),
            ],
            options={
                'verbose_name': 'Lieferobjekt',
                'verbose_name_plural': 'Lieferobjekte',
            },
        ),
        migrations.AlterModelOptions(
            name='specialroles',
            options={'permissions': (('is_operations_group', 'Benutzer ist in der BG'), ('is_book_keeper', 'Benutzer ist Buchhalter'), ('new_subscription', 'Benutzer über Abobestellungen informieren'), ('can_send_mails', 'Benutzer kann im System Emails versenden'), ('can_use_general_email', 'Benutzer kann General Email Adresse verwenden'))},
        ),
        migrations.RemoveField(
            model_name='member',
            name='block_emails',
        ),
        migrations.AddField(
            model_name='member',
            name='cancelation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Kündigüngssdatum'),
        ),
        migrations.AddField(
            model_name='member',
            name='canceled',
            field=models.BooleanField(default=False, verbose_name='gekündigt'),
        ),
        migrations.AddField(
            model_name='member',
            name='future_subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members_future', to='juntagrico.Subscription'),
        ),
        migrations.AddField(
            model_name='member',
            name='iban',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='IBAN'),
        ),
        migrations.AddField(
            model_name='member',
            name='inactive',
            field=models.BooleanField(default=False, verbose_name='inaktiv'),
        ),
        migrations.AddField(
            model_name='member',
            name='old_subscriptions',
            field=models.ManyToManyField(related_name='members_old', to='juntagrico.Subscription'),
        ),
        migrations.AlterField(
            model_name='activityarea',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='delivery',
            unique_together=set([('delivery_date', 'subscription_size')]),
        ),
    ]
