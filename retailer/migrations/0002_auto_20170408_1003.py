# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='delivery_time',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='manufacturig_time',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
