# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 14:02

import model_utils.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='status',
            field=model_utils.fields.StatusField(
                default='modified',
                help_text='modified means the configuration is not applied yet; running means applied and running; error means the configuration caused issues and it was rolledback',
                max_length=100,
                no_check_for_status=True,
            ),
        ),
    ]
