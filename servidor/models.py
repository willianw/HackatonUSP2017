# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.fields.related import *



# Create your models here.

class Pesquisador(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.ForeignKey(Instituicao, null=True)
    area_conhecimento = models.ForeignKey(MediasAreas, null=True)
    nivel = models.CharField(max_length=100)


    def __str__(self):
        return self.nome(self)

class Instituicao(models.Model):
    nome = models.CharField(max_length=200)
    area = models.ForeignKey(GrandesAreas,  null=True)
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome(self)

class GrandesAreas(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome(self)

class MediasAreas(models.Model):
    nome = models.CharField(max_length=100)
    grande_area = models.ForeignKey(GrandesAreas, null=True)

    def __str__(self):
        return self.nome(self)

class PequenasAreas(models.Model):
    nome = models.CharField(max_length=100)
    media_area = models.ForeignKey(MediasAreas, null=True)

    def __str__(self):
        return self.nome(self)

class Pesquisa(models.Model):
    pesquisadores = models.ManytoMany(Pesquisador)
    pequena_area = models.ForeignKey(PequenasAreas, null=True)
    abstract = models.TextField()
    tags = models.TextField()

