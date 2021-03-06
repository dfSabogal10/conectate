# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 04:12
from __future__ import unicode_literals

import cuser.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('herramienta', '0007_fileuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='HerramientasPorAprobar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('herramienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herramienta.Herramienta')),
                ('owner', cuser.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='herramienta_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
