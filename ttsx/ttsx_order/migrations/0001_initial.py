# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userInfo', '0002_auto_20180212_1039'),
        ('ttsx_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cont', models.IntegerField()),
                ('pric', models.DecimalField(max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(to='ttsx_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('order_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('set_time', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('user', models.ForeignKey(to='userInfo.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='ttsx_order.OrderMain'),
        ),
    ]
