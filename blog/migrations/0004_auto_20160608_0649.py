# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='photo2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='shop',
            name='photo3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
