# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0019_auto_20150824_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='form_asociado',
            field=models.ForeignKey(blank=True, to='registro.Formulario', null=True),
        ),
    ]
