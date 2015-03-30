from django.db import models

# Create your models here.
class Preguntas(models.Model):
	nombres = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	pregunta1 = models.CharField(max_length=500)
	pregunta2 = models.CharField(max_length=500)
	pregunta3 = models.CharField(max_length=500)
	pregunta4 = models.CharField(max_length=500)
	pregunta5 = models.CharField(max_length=500)
	pregunta6 = models.CharField(max_length=500)
	pregunta7 = models.CharField(max_length=500)
	pregunta8 = models.CharField(max_length=500)
	pregunta9 = models.CharField(max_length=500)
	pregunta10 = models.CharField(max_length=500)
	conclusion = models.CharField(max_length=500)
	imagen = models.ImageField()
	fecha = models.DateTimeField()		