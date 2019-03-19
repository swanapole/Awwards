# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_colors'),
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['countries'],
            },
        ),
    ]
