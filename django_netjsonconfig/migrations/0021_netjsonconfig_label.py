# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0020_openvpn_resolv_retry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='backend',
            field=models.CharField(
                choices=[
                    ('netjsonconfig.OpenWrt', 'OpenWRT'),
                    ('netjsonconfig.OpenWisp', 'OpenWISP Firmware 1.x'),
                ],
                help_text='Select <a href="http://netjsonconfig.openwisp.org/en/stable/" target="_blank">netjsonconfig</a> backend',
                max_length=128,
                verbose_name='backend',
            ),
        ),
        migrations.AlterField(
            model_name='template',
            name='backend',
            field=models.CharField(
                choices=[
                    ('netjsonconfig.OpenWrt', 'OpenWRT'),
                    ('netjsonconfig.OpenWisp', 'OpenWISP Firmware 1.x'),
                ],
                help_text='Select <a href="http://netjsonconfig.openwisp.org/en/stable/" target="_blank">netjsonconfig</a> backend',
                max_length=128,
                verbose_name='backend',
            ),
        ),
    ]