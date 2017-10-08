# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171008_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/images/avatars/', verbose_name='profile picture'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
