# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-04 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyas2', '0016_auto_20161004_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='mdn',
            field=models.BooleanField(default=False, verbose_name='Request MDN'),
        ),
    ]
