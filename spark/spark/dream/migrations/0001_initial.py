# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-15 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import dream.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=dream.models.get_image_path)),
            ],
        ),
    ]
