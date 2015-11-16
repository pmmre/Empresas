from django.conf.urls import include, url
from .views import index,registrar,borrar,calificar,listar,ranking,borrarEmpresa

urlpatterns = [
	url(r'^$', index.as_view(), name="empresa"),
	url(r'^registrar$', registrar.as_view(), name="registrar"),
	url(r'^borrar$', borrar.as_view(), name="borrar"),
	url(r'^calificar$', calificar.as_view(), name="calificar"),
	url(r'^listar$', listar.as_view(), name="listar"),
	url(r'^ranking$', ranking.as_view(), name="ranking"),
	url(r'^borrarEmpresa$', borrarEmpresa.as_view(), name="borrarEmpresa"),
]
