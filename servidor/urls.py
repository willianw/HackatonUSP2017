from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='Home Page'),
    url(r'search', views.simple_search, name='Simple Search'),
	url(r'researcher', views.pesquisador_search, name='Researcher Search'),
	url(r'research', views.pesquisa_search, name='Research Search'),
	url(r'pesquisador', views.pesquisador_view, name='Researcher View'),
]
