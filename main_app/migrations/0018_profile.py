# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-13 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_remove_treasure_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name', max_length=50)),
                ('last_name', models.CharField(db_column='last_name', max_length=50)),
            ],
        ),
    ]
