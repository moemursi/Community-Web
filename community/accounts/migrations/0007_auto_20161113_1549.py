# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20161113_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_image', to='accounts.ProfileImage'),
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_image', to='accounts.Profile'),
        ),
    ]
