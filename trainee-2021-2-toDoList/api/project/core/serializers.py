from rest_framework import serializers
from core.models import *

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'
        
class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarefa
        fields = '__all__'

