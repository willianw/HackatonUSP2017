# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pymongo import MongoClient
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	client = MongoClient('localhost', 27017)
	context = client['database-hackaton'].professores.find_one()
	print context
	print context['nome']
	return render(request, 'index.html', context)
