# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-29 06:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
