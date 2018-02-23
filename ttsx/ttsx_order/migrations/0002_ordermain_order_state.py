# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='order_state',
            field=models.BooleanField(default=False),
        ),
    ]
