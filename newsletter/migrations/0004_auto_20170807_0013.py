# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20170807_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
