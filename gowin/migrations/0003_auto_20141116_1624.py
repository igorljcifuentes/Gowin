# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gowin', '0002_auto_20141116_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='nombres',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
    ]
