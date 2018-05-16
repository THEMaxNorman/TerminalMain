# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-15 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0009_posting_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum_post',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='forum_topic',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]