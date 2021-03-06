# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-18 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170214_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.Group'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_event_image', to='events.EventImage'),
        ),
    ]
