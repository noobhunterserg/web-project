# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
