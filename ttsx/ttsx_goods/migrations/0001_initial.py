# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gname', models.CharField(max_length=20)),
                ('gimg', models.ImageField(upload_to=b'goods/')),
                ('gpric', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gclicks', models.IntegerField(default=0)),
                ('gmete', models.CharField(max_length=20)),
                ('isdelete', models.BooleanField(default=False)),
                ('gsubtitle', models.CharField(max_length=200)),
                ('gkucun', models.IntegerField(verbose_name=100)),
                ('gcount', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tname', models.CharField(max_length=20)),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='ttsx_goods.GoodsType'),
        ),
    ]
