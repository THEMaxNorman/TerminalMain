# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-15 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0010_auto_20180515_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='catergory',
            field=models.CharField(blank=True, choices=[('Free', 'Free'), ('For Sale', 'For Sale'), ('Currency Exchange', 'Currency Exchange'), ('Wanted', 'Wanted')], max_length=40),
        ),
    ]
