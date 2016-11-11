# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 08:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('communities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=512, null=True)),
                ('max_attendees', models.IntegerField(blank=True, null=True)),
                ('private', models.BooleanField(default=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.Community')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeetupAttendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Going', max_length=200)),
                ('signup_time', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('meetup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.Meetup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='meetup',
            unique_together=set([('community', 'creator', 'created_date')]),
        ),
    ]
