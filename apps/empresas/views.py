from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,View
from .models import Empresa
from django.core.urlresolvers import reverse_lazy
import sqlite3


## Create your views here.


class index(CreateView):
	template_name = 'empresas/index.html'
	model = Empresa
	fields = ['nombre','calificacion']


	


class borrar(CreateView):
	template_name = 'empresas/borrar.html'
	model = Empresa
	fields = ['nombre','calificacion']
	success_url = reverse_lazy('empresa')

	def post(self, request, *args, **kwargs):
		borrar = request.POST['NB']

		if Empresa.objects.filter(nombre=borrar):
			emp = Empresa.objects.get(nombre=borrar)
			emp.calificacion=-1
			emp.save()
			borrar = "A la empresa "+borrar+ " se le ha eliminado la calificacion"
		else:
			borrar = "La empresa "+borrar+ " no existe"
		
		return render(request,'empresas/borrar.html',{'borrar':borrar})

	

class registrar(CreateView):
	template_name = 'empresas/registrar.html'
	model = Empresa
	fields = ['nombre','calificacion']
	success_url = reverse_lazy('empresa')

	def post(self, request, *args, **kwargs):
		nombre_empresa = request.POST['nombre']
		emp = Empresa.objects.filter(nombre=nombre_empresa)
		if emp:
			salida="Empresa "+nombre_empresa+" ya esta creada."
		else:
			emp = Empresa(nombre=nombre_empresa,calificacion="-1")
			emp.save()
			salida="Empresa "+nombre_empresa+" ACABA DE CREARSE."
		
		
		return render(request,'empresas/registrar.html',{'salida':salida})

class calificar(ListView):
	template_name = 'empresas/calificar.html'
	model = Empresa
	#fields = ['nombre','calificacion']
	success_url = reverse_lazy('empresa')

	def post(self, request, *args, **kwargs):
		nombre_empresa = request.POST['nombre']
		calificacion2 = request.POST['calificacion']
		if Empresa.objects.filter(nombre=nombre_empresa): 
			emp = Empresa.objects.get(nombre=nombre_empresa)
			if emp.calificacion==-1:
				if int(calificacion2)>=0 or int(calificacion2)<=10:
					emp.calificacion=calificacion2
					emp.save()
					salida="La empresa "+nombre_empresa+" ha sido calificada con un "+calificacion2+"."
				else:
					salida="La calificacion debe de estar entre 0 y 10."
			else:
				salida="La empresa "+nombre_empresa+" ya ha sido calificada"			
		else:
			salida="La empresa "+nombre_empresa+" no existe."

		
		return render(request,'empresas/calificar.html',{'salida':salida})


class listar(ListView):
	template_name = 'empresas/listar.html'
	model = Empresa
	#fields = ['nombre','calificacion']
	success_url = reverse_lazy('empresa')


class ranking(CreateView):
	template_name = 'empresas/ranking.html'
	model = Empresa
	fields = ['nombre','calificacion']
	success_url = reverse_lazy('empresa')

	def get(self, request, *args, **kwargs):
		ordenado = Empresa.objects.order_by('calificacion').reverse
		
		return render(request,'empresas/ranking.html',{'ordenado':ordenado})

	
	
class borrarEmpresa(CreateView):
	template_name = 'empresas/borrarEmpresa.html'
	model = Empresa
	fields = ['nombre','calificacion']
	success_url = reverse_lazy('empresa')

	def post(self, request, *args, **kwargs):
		borrar = request.POST['NB']
		
		if Empresa.objects.filter(nombre=borrar):
			Empresa.objects.filter(nombre=borrar).delete()
			borrar = "La empresa "+borrar+ " ha sido borrada con exito"
		else:
			borrar = "La empresa "+borrar+ " no existe, por lo tanto, NO PUEDE SER BORRADA"
		ordenado = Empresa.objects.order_by('calificacion').reverse
		
		return render(request,'empresas/borrarEmpresa.html',{'ordenado':ordenado, 'borrar':borrar})



