# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('update_status', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UpStatus',
        ),
    ]
