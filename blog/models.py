# AGREGAR ARCHIVOS 
from django.db 	  import models
from django.utils import timezone

class Post(models.Model):							# Define el modelo (objeto) Post => NombreModelo 
	author = models.ForeignKey('auth.User')		
	tittle = models.CharField(max_length=200)		# models.CharField => texto con numero limitado de caracteres
	text   = models.TextField()
	created_date = models.DateTimeField(
		default = timezone.now)
	published_date=models.DateTimeField(
		blank = True, null = True)
		
	def publish(self):								# Metodo publish 
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.tittle 
