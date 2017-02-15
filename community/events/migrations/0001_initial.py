# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 00:03
from __future__ import unicode_literals

import community.events.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, default=django.utils.timezone.now, verbose_name='date created')),
                ('start_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('end_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=2048, null=True)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('private', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.Community')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventAttendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signup_time', models.DateTimeField(auto_created=True, verbose_name='date joined')),
                ('status', models.CharField(choices=[('GOING', 'going'), ('INTERESTED', 'interested'), ('NOT_GOING', 'not going')], default='GOING', max_length=200)),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='last updated')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_attendee', to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=community.events.models.get_event_image_path)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_image', to='events.Event')),
            ],
        ),
    ]
