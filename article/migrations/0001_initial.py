# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-09 15:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('body', models.TextField(default='', verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('created_time', models.DateTimeField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_time', models.DateTimeField(verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='\u6458\u8981')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u8005')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u7c7b\u522b\u540d\u79f0')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u6807\u7b7e\u540d\u79f0')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Category', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='article.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]