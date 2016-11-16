# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 03:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('communities', '0009_auto_20161106_2234'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_created=True, verbose_name='date created')),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('create_by', models.CharField(blank=True, max_length=30, null=True)),
                ('current_leader', models.CharField(blank=True, max_length=30, null=True)),
                ('title', models.CharField(max_length=50)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.Community')),
            ],
        ),
        migrations.CreateModel(
            name='Group_Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(auto_created=True, verbose_name='date joined')),
                ('position', models.CharField(blank=True, max_length=30, null=True)),
                ('last_activity', models.CharField(blank=True, max_length=300, null=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.Community')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='group_members',
            unique_together=set([('user', 'id', 'community', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('community', 'id')]),
        ),
    ]
