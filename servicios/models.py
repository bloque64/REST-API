from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
    
    
    
class Publicacion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=180)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=20)
    evaluado = models.BooleanField(default=False)
    formateado = models.BooleanField(default=False)
    curado = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    
class Steemit(models.Model):
    publicado_fecha = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=180)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=20)
    votado = models.BooleanField(default=False)
    publicado = models.BooleanField(default=False)

    class Meta:
        ordering = ('publicado_fecha',)
