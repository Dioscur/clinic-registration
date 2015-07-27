# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0003_auto_20150727_0138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='medic_name',
            new_name='medic',
        ),
        migrations.AlterField(
            model_name='record',
            name='medic_name',
            field=models.ForeignKey(to='regist.Doctors'),
        ),
    ]
