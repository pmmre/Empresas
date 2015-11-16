from django.test import TestCase
from .models import Empresa
from .views import registrar
from django.shortcuts import render
from django.test.client import Client
from django.core.urlresolvers import reverse
 

# Create your tests here.
import unittest


class TestStringMethods(unittest.TestCase):

	def test_Modelo(self):
		"""
			Probando insercciones de la base de datos.
		"""
		emp = Empresa(nombre="Maracena",calificacion="-1")
		emp.save()

		emp2 = Empresa.objects.get(nombre="Maracena")
		#self.assertEqual(emp,Empresa.objects.filter(nombre="Maracena"))
		self.assertEqual(emp.nombre,emp2.nombre)
		self.assertEqual(int(emp.calificacion),int(emp2.calificacion))

	def test_funciona_index(self):
		c = Client()

		response = c.get(reverse('empresa'))
		self.assertEqual(response.status_code, 200)

	def test_funciona_registrar(self):
		"""
			Este Test prueba que funcionan correctamente la vista encargada
			de registrar empresas en la aplicacion. 
			Primero se crea un cliente con el hago una peticion por post
			a registra. 
			Una vez hecho compruebo que se ha hecho correctamente y ademas 
			que se ha hecho la inserccion en la base de datos correctamente.
			Luego intento registrar la misma empresa y comprubo que va bien
			y no se ha introducido dos veces (objects.get solo devuelve un 
			valor).
		"""
		c = Client()

		response = c.post(reverse('registrar'),{'nombre':"Mercadona"})
		self.assertEqual(response.status_code, 200)
		emp = Empresa.objects.get(nombre="Mercadona")
		self.assertEqual(emp.nombre,"Mercadona")

		response = c.post(reverse('registrar'),{'nombre':"Mercadona"})
		self.assertEqual(response.status_code, 200)
		emp = Empresa.objects.get(nombre="Mercadona")

	def test_funciona_borrar(self):
		"""
			En el siguiente test creo un empresa con calificacion 8,
			la guardo en la base de datos, obtengo la tupla de la base
			de datos y compruebo que lo introducido es correcto.
			Una vez hecho esto llamo a borrar que eliminara la calificacion,
			vuelvo a obtener de la base de datos y compruebo que efectivamente
			se ha eliminado la calificacion (en mi caso -1) y vuelvo a
			llamar a borrar para saber si hace una peticion bien aunque
			ya este la calificacion a -1.
		"""
		c = Client()

		emp = Empresa(nombre="Mercadona",calificacion="8")
		emp.save()
		emp = Empresa.objects.get(nombre="Mercadona")
		self.assertEqual(emp.nombre,"Mercadona")
		self.assertEqual(emp.calificacion,8)

		response = c.post(reverse('borrar'),{'NB':"Mercadona"})
		self.assertEqual(response.status_code, 200)
		emp = Empresa.objects.get(nombre="Mercadona")
		self.assertEqual(emp.calificacion,-1)

		response = c.post(reverse('borrar'),{'NB':"Mercadona"})
		self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
	unittest.main()


