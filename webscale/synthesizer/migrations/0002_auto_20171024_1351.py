# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synthesizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationtable',
            name='client_secret',
            field=models.CharField(max_length=200, verbose_name='Client Secret'),
        ),
        migrations.AlterField(
            model_name='applicationtable',
            name='contact_email',
            field=models.EmailField(help_text='Enter your email', max_length=200, verbose_name='Contact Email'),
        ),
        migrations.AlterField(
            model_name='applicationtable',
            name='copyright_date',
            field=models.CharField(help_text='Enter copyright date', max_length=200, verbose_name='Copyright Date'),
        ),
    ]
