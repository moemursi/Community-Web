# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_auto_20161106_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityuserprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
