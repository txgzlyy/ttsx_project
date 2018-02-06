# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('pass_word', models.CharField(max_length=40)),
                ('tel_num', models.CharField(max_length=11)),
                ('emails', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('you_bian', models.CharField(max_length=20)),
            ],
        ),
    ]
