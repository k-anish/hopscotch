# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retailer', '0004_men_occasion_packages_same_day_women'),
    ]

    operations = [
        migrations.CreateModel(
            name='Men_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Products')),
                ('submenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Men')),
            ],
        ),
        migrations.CreateModel(
            name='Packages_pack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Women_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Products')),
                ('submenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Women')),
            ],
        ),
        migrations.RemoveField(
            model_name='packages',
            name='product',
        ),
        migrations.AddField(
            model_name='packages',
            name='combo_price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='same_day',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Products'),
        ),
    ]
