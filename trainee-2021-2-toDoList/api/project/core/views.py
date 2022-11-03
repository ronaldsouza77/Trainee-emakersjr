from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# CRUD CATEGORIA

class ListCategoria(generics.ListAPIView):              #Read Categoria
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class DetailCategoria(generics.ListAPIView):            #Update Categoria
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CreateCategoria(generics.ListAPIView):            #Create Categoria
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class DeleteCategoria(generics.ListAPIView):            #Delete Categoria
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

#CRUD TAREFA

class ListTarefa(generics.ListAPIView):              #Read Tarefa
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class DetailTarefa(generics.RetrieveUpdateAPIView):  #Update Tarefa
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class CreateTarefa(generics.CreateAPIView):          #Create Tarefa
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class DeleteTarefa(generics.DestroyAPIView):         #Delete Tarefa
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
