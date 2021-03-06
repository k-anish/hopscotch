# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 09:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=31)),
                ('lname', models.CharField(max_length=31)),
                ('email', models.EmailField(max_length=31, unique=True)),
                ('phone', models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator('^[7,8,9]{1}[0-9]{9}$', 'The given phone number does not exist in India')])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1)),
                ('bank_account_number', models.IntegerField()),
                ('password', models.CharField(max_length=31)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=1023)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Data')),
            ],
        ),
        migrations.CreateModel(
            name='Shortcomings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(validators=[django.core.validators.RegexValidator('^[1,2,3,4,5]$', 'Rating must be between 1-5')])),
                ('comment', models.CharField(max_length=127)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.Data')),
            ],
        ),
    ]
