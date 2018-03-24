from django.contrib import admin
from .models import Post				# Se importa el modelo post

admin.site.register(Post)				# Hacer el modelo visible en la pag de administrador
