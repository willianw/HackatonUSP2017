# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 00:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0005_graudeinstrucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisador',
            name='nivel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servidor.GrauDeInstrucao'),
        ),
    ]
