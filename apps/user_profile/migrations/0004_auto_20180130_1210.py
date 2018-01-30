# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-30 12:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to=settings.AUTH_USER_MODEL),
        ),
    ]
