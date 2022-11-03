from asyncio.windows_events import NULL
from django.db import models
from django.conf import settings

class Categoria(models.Model):
    titulo = models.CharField(max_length = 100,
                              unique = True,
                              blank = False) 

class Tarefa(models.Model):
    titulo = models.CharField(
                              max_length = 200,
                              unique = True,
                              blank = False
                             ) 
    descricao = models.TextField() 
    prazo = models.DateTimeField()
    categoria = models.ForeignKey(
                                  Categoria, 
                                  related_name='Tarefa',
                                  default = 0,
                                  on_delete = models.SET_DEFAULT
                                 )
    concluida = models.BooleanField(default = False)

