# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_signup_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
