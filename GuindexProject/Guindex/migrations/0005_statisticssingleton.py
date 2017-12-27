# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 12:01
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guindex', '0004_auto_20171226_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticsSingleton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubsInDb', models.IntegerField(default=0)),
                ('averagePrice', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=6)),
                ('standardDevation', models.DecimalField(decimal_places=3, default=Decimal('0.0'), max_digits=12)),
                ('percentageVisited', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=5)),
                ('closedPubs', models.IntegerField(default=0)),
                ('notServingGuinness', models.IntegerField(default=0)),
                ('lastCalculated', models.DateTimeField(auto_now=True)),
                ('cheapestPub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cheapest_pub', to='Guindex.Pub')),
                ('dearestPub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dearest_pub', to='Guindex.Pub')),
            ],
        ),
    ]
