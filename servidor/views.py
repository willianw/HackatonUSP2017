# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
	context = {
		'institutos': Instituicao.objects.all(),
		'pequenas_areas': PequenasAreas.objects.all(),
		'niveis': GrauDeInstrucao.objects.all(),
		'areas_conhecimento': MediasAreas.objects.all()}
	return render(request, 'testeo.html', context)

def simple_search(request):
	if request.method == 'GET':
		return render(request, 'busca.html')
	else:
		query = request.POST['query']
		context = {
			'status': 200,
			'query': query,
			'titulo': Pesquisa.objects.filter(nome__icontains=query),
			'pesquisador': Pesquisa.objects.filter(pesquisadores__nome__icontains=query),
			'pequena_area': Pesquisa.objects.filter(pequena_area__nome__icontains=query),
			'abstract': Pesquisa.objects.filter(abstract__icontains=query),
			'tags': Pesquisa.objects.filter(tags__icontains=query),
		}
		print "context:", context
		return render(request, 'ResultadoBusca.html', context)

def pesquisador_search(request):
	if request.method == 'GET':
		return render(request, 'busca.html', {'institutos':Instituicao.objects.all(), 'areas_conhecimento': MediasAreas.objects.all()})
	else:
		nome = request.POST['nome']
		instituto = request.POST['instituto']
		area_conhecimento = request.POST['area_conhecimento']

		result = Pesquisador.objects.all()
		if nome:
			result = result.filter(nome__icontains=nome)
		if instituto:
			result = result.filter(instituicao__id__exact=instituto)
		if area_conhecimento:
			result = result.filter(area_conhecimento__id__exact=area_conhecimento)

		context = {
			'professores': result
		}
		return render(request, 'list_professores.html', context)

def pesquisa_search(request):
	if request.method == 'GET':
		return render(request, 'busca.html', {'institutos':Instituicao.objects.all(), 'areas_conhecimento': MediasAreas.objects.all()})
	else:
		titulo = request.POST['nome']
		pequena_area = request.POST['pequena_area']
		nivel = request.POST['nivel']
		abstract = request.POST['abstract']
		tags = request.POST['tags']

		result = Pesquisador.objects.all()
		if titulo:
			result = result.filter(nome__icontains=titulo)
		if pequena_area:
			result = result.filter(pequena_area__id__exact=pequena_area)
		if nivel:
			result = result.filter(nivel__id__exact=nivel)
		if abstract:
			result = result.filter(abstract__icontains=abstract)
		if tags:
			result = result.filter(tags__icontains=tags)


		context = {
			'pesquisas': result
		}
		return render(request, 'pesquisador_search.html', context)

def pesquisador_view(request):
	id = request.GET['id']
	pesquisador = Pesquisador.objects.get(id__exact=id)
	context = {
		'pesquisador': pesquisador,
		'pesquisas': Pesquisa.objects.filter(pesquisadores__id = id)
	}
	print context
	return render(request, 'PerfilPesquisador.html', context)

def instituto_view(request):
	id = request.GET['instituto']
	instituto = Instituicao.objects.get(id__exact=id)
	context = {
		'instituto': instituto,
		'pesquisadores': Pesquisador.objects.filter(instituicao__id=id)
	}
	print context
	return render(request, 'PerfilInstituto.html', context)
