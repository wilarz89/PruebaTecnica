# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.CharField(max_length=10000)),
                ('salida', models.CharField(max_length=10000)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
