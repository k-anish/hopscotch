# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retailer', '0003_products_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submenu', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submenu', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Data')),
            ],
        ),
        migrations.CreateModel(
            name='Same_day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Data')),
            ],
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submenu', models.CharField(max_length=15)),
            ],
        ),
    ]
