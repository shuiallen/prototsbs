# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StitchingRecord',
            new_name='PanelStitchingRecord',
        ),
    ]
