# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_userfriend_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfriend',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
