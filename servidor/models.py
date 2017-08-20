# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.fields.related import *



# Create your models here.


class Modelo(models.Model):
	id = models.AutoField(primary_key=True)
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
	sala = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	area_conhecimento = models.ForeignKey(MediasAreas, null=True)
	nivel = models.ForeignKey(GrauDeInstrucao, null=True)

class Pesquisa(Modelo):
	pesquisadores = models.ManyToManyField(Pesquisador)
	titulo = models.TextField(null=True)
	start = models.IntegerField(null=True)
	end = models.IntegerField(null=True)
	pequena_area = models.ForeignKey(PequenasAreas, null=True)
	nivel = models.ForeignKey(GrauDeInstrucao, null=True)
	abstract = models.TextField()
	tags = models.TextField()
	bibliografia = models.ManyToManyField("self", blank=True)

	@property
	def citacoes_diretas(self):
		i = 0
		for pesquisa in Pesquisa.objects.all():
			if self in pesquisa.bibliografia:
				i = i + 1
		return i
