# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 14:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('landing_page', models.ImageField(upload_to='landingpage/')),
                ('description', tinymce.models.HTMLField()),
                ('link', models.CharField(max_length=255)),
                ('screenshot1', models.ImageField(upload_to='screenshots/')),
                ('screenshot2', models.ImageField(upload_to='screenshots/')),
                ('screenshot3', models.ImageField(upload_to='screenshots/')),
                ('screenshot4', models.ImageField(upload_to='screenshots/')),
                ('design', models.IntegerField(blank=True, default=0)),
                ('usability', models.IntegerField(blank=True, default=0)),
                ('creativity', models.IntegerField(blank=True, default=0)),
                ('content', models.IntegerField(blank=True, default=0)),
                ('overall_score', models.IntegerField(blank=True, default=0)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('categories', models.ManyToManyField(to='projects.categories')),
                ('colors', models.ManyToManyField(to='projects.colors')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.countries')),
                ('technologies', models.ManyToManyField(to='projects.technologies')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
