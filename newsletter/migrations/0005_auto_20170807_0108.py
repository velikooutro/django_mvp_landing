# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20170807_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(default=datetime.date.today, null=True, blank=True),
        ),
    ]
