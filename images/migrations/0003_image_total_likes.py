# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-07 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20171206_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
