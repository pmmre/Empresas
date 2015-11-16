# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20151020_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='calificacion',
            field=models.IntegerField(default=-1),
        ),
    ]
