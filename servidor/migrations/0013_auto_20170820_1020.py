# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 10:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0012_auto_20170820_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campus',
            old_name='_id',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='grandesareas',
            old_name='_id',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='graudeinstrucao',
            old_name='_id',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='instituicao',
            old_name='_id',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='mediasareas',
            old_name='_id',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='pequenasareas',
            old_name='_id',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='pesquisa',
            old_name='_id',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='pesquisador',
            old_name='_id',
            new_name='pid',
        ),
    ]