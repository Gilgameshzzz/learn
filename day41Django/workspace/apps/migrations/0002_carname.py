# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-10 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=10, unique=True)),
                ('c_age', models.IntegerField(default=16)),
                ('c_year', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'CarName',
            },
        ),
    ]
