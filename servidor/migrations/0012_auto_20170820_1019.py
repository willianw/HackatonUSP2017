# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 10:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0011_auto_20170820_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campus',
            old_name='id',
            new_name='_id',
        ),
        migrations.RenameField(
            model_name='grandesareas',
            old_name='id',
            new_name='_id',
        ),
        migrations.RenameField(
            model_name='graudeinstrucao',
            old_name='id',
            new_name='_id',
        ),
        migrations.RenameField(
            model_name='instituicao',
            old_name='id',
            new_name='_id',
        ),
        migrations.RenameField(
            model_name='mediasareas',
            old_name='id',
            new_name='_id',
        ),
        migrations.RenameField(
            model_name='pequenasareas',
            old_name='id',
            new_name='_id',
        ),
        migrations.RenameField(
            model_name='pesquisa',
            old_name='id',
            new_name='_id',
        ),
        migrations.RenameField(
            model_name='pesquisador',
            old_name='id',
            new_name='_id',
        ),
    ]
