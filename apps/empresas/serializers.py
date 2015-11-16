from rest_framework import serializers
from apps.models import Empresa


class EmpresaSerializer(models.Model):
	nombre = serializers.CharField(max_length=50)
	calificacion = serializers.IntegerField(default=-1)

