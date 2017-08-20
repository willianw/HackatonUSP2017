# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def simple_search(request):
	query = 'FAU'
	context = {
		'status': 200,
		'titulo': Pesquisa.objects.filter(nome__icontains=query),
		'pequena_area': Pesquisa.objects.filter(pequena_area__nome__icontains=query),
		'abstract': Pesquisa.objects.filter(abstract__icontains=query),
		'tags': Pesquisa.objects.filter(tags__icontains=query),
	}
	print context
	return render(request, 'index.html', context)
