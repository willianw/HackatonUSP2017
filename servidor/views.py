# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	context = client['database-hackaton'].professores.find_one()
	print context
	print context['nome']
	return render(request, 'index.html', context)
