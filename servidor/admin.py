# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pesquisador, Campus, Instituicao, GrauDeInstrucao, GrandesAreas, MediasAreas, PequenasAreas, Pesquisa

# Register your models here.
admin.site.register(Pesquisador)
admin.site.register(Campus)
admin.site.register(Instituicao)
admin.site.register(GrandesAreas)
admin.site.register(MediasAreas)
admin.site.register(PequenasAreas)
admin.site.register(Pesquisa)
admin.site.register(GrauDeInstrucao)
