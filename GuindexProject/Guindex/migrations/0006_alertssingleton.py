# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guindex', '0005_statisticssingleton'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertsSingleton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastAlertCheck', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]