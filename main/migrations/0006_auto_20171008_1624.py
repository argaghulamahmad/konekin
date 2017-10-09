# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171008_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='static/img/noprofile.svg', null=True, upload_to='static/media/images/avatars/', verbose_name='profile picture'),
        ),
    ]