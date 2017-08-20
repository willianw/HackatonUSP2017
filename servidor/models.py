# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.fields.related import *



# Create your models here.


class Modelo(models.Model):
	nome = models.CharField(max_length=100, blank=True, null=True, default="nome")
	def __unicode__ (self):
		return self.nome.encode('utf-8')

	def __str__(self):
		return self.nome

	class Meta:
		abstract=True

class GrandesAreas(Modelo):
	pass
 # 	tipo = models.CharField(max_length=100)

class MediasAreas(Modelo):
	grande_area = models.ForeignKey(GrandesAreas, null=True)

class PequenasAreas(Modelo):
	media_area = models.ForeignKey(MediasAreas, null=True)

class Campus(Modelo):
	pass

class Instituicao(Modelo):
    area = models.ForeignKey(GrandesAreas,  null=True)
    localizacao = models.ForeignKey(Campus, null=True)
    #departamentos = models.ManyToManyField(Departamentos)

class GrauDeInstrucao(Modelo):
    pass

class Pesquisador(Modelo):
	instituicao = models.ForeignKey(Instituicao, null=True)
	area_conhecimento = models.ForeignKey(MediasAreas, null=True)
	nivel = models.ForeignKey(GrauDeInstrucao, null=True)
	# def __unicode__ (self):
	# 	return self.nivel.encode('utf-8')

class Pesquisa(Modelo):
    pesquisadores = models.ManyToManyField(Pesquisador)
    pequena_area = models.ForeignKey(PequenasAreas, null=True)
    abstract = models.TextField()
    tags = models.TextField()
	# def __unicode__ (self):
	# 	return self.abstract.encode('utf-8')
	# def __unicode__ (self):
	# 	return self.nivel.encode('utf-8')

