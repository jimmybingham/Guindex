# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guindex', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pub',
            name='creationDate',
        ),
        migrations.RemoveField(
            model_name='pub',
            name='creator',
        ),
    ]
