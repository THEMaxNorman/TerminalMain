# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-30 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0003_massage'),
    ]

    operations = [
        migrations.AddField(
            model_name='massage',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
