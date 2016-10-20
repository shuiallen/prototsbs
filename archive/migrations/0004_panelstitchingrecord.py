# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_auto_20160511_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='PanelStitchingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignedDate', models.DateField()),
                ('receivedDate', models.DateField()),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Panel')),
                ('stitcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Participant')),
            ],
        ),
    ]
