from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'search', views.simple_search, name='Simple Search'),
	url(r'researcher', views.pesquisador_search, name='Researcher Search'),
	url(r'research', views.pesquisa_search, name='Research Search'),
]
