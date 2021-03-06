# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-18 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Please provide your first and last names', max_length=250)),
                ('phone', models.IntegerField(help_text='Provide contact number with country code!')),
                ('email', models.EmailField(help_text='Email', max_length=254)),
                ('comment', models.TextField(help_text='What is the nature of your inquiry/problem')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
