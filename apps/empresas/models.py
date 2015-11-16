from django.db import models

# Create your models here.

class Empresa(models.Model):
	nombre = models.CharField(max_length=50)
	calificacion = models.IntegerField(default=-1)

	def __unicode__(self):
		return self.nombre


