# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesquisador',
            name='instituicao',
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='nome',
            field=models.CharField(blank=True, default='nome', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='grandesareas',
            name='nome',
            field=models.CharField(blank=True, default='nome', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='localizacao',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='nome',
            field=models.CharField(blank=True, default='nome', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mediasareas',
            name='nome',
            field=models.CharField(blank=True, default='nome', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pequenasareas',
            name='nome',
            field=models.CharField(blank=True, default='nome', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pesquisador',
            name='nivel',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pesquisador',
            name='nome',
            field=models.CharField(blank=True, default='nome', max_length=100, null=True),
        ),
    ]
