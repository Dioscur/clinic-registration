# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('medic_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='record',
            name='medic_name',
            field=models.ForeignKey(to='regist.Doctors'),
        ),
    ]
