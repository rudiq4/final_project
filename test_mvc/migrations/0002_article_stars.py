# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('test_mvc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='stars',
            field=models.FloatField(default=0.0, verbose_name='Rating'),
        ),
    ]