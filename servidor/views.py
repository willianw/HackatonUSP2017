# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def simple_search(request):
	query = 'condimentum'
	context = {
		'status': 200,
		'query': query,
		'titulo': Pesquisa.objects.filter(nome__icontains=query),
		'pesquisador': Pesquisa.objects.filter
		'pequena_area': Pesquisa.objects.filter(pequena_area__nome__icontains=query),
		'abstract': Pesquisa.objects.filter(abstract__icontains=query),
		'tags': Pesquisa.objects.filter(tags__icontains=query),
	}
	print context
	return render(request, 'simple_search_be.html', context)
