# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synthesizer', '0005_snippit_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='googleauth',
            name='is_authenticated',
            field=models.BooleanField(default=True, help_text='Boolean for if user has authorized access to Drive.'),
        ),
    ]
