# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0002_auto_20150727_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='medic_name',
            field=models.CharField(max_length=100),
        ),
    ]
