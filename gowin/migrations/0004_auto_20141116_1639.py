# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gowin', '0003_auto_20141116_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas',
            name='apellidos',
            field=models.CharField(max_length=200, default=datetime.datetime(2014, 11, 16, 19, 39, 9, 434089, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='conclusion',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 19, 876687, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 16, 19, 39, 22, 843856, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='imagen',
            field=models.ImageField(upload_to='', default=datetime.datetime(2014, 11, 16, 19, 39, 26, 750080, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta1',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 28, 881202, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta10',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 34, 544526, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta2',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 38, 287740, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta3',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 40, 429862, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta4',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 45, 429148, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta5',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 49, 660390, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta6',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 52, 232537, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta7',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 54, 442664, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta8',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 56, 855802, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preguntas',
            name='pregunta9',
            field=models.CharField(max_length=500, default=datetime.datetime(2014, 11, 16, 19, 39, 59, 989981, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='nombres',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
