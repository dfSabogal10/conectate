# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-17 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramienta', '0015_auto_20180512_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejemplo',
            name='herramienta',
        ),
        migrations.AddField(
            model_name='ejemplo',
            name='herramienta',
            field=models.ManyToManyField(to='herramienta.Herramienta'),
        ),
    ]
