# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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
		return render(request, 'simple_search_be.html', context)

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
			'pesquisadores': result
		}
		return render(request, 'pesquisador_search.html', context)
