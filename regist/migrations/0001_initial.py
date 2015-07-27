# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('medic_name', models.CharField(max_length=100)),
                ('visitor_first_name', models.CharField(max_length=50)),
                ('visitor_last_name', models.CharField(max_length=50)),
                ('record_date', models.DateField()),
                ('record_time', models.TimeField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
