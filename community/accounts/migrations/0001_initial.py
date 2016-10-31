# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 17:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=60, null=True)),
                ('department', models.CharField(blank=True, max_length=60, null=True)),
                ('interests', models.CharField(blank=True, max_length=60, null=True)),
                ('transportation', models.CharField(blank=True, max_length=60, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
