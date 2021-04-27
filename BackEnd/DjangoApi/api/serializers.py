from django.contrib.auth.models import User, Group
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import *


class tarjetaSerializer(serializers.ModelSerializer):
    ciudadnombre = serializers.CharField(
        source='ciudad.nombre',
        read_only=True
    )

    class Meta:
        model = tarjeta
        fields = ['ciudadnombre', 'ciudad_id', 'id', 'titular',
                  'numeroTarjeta', 'fechaExpiracion', 'cvv']


class personaSerializer(serializers.ModelSerializer):
    ciudadnombre = serializers.CharField(
        source='ciudad.nombre',
        read_only=True
    )

    class Meta:
        model = persona
        fields = ['nombre', 'direccion', 'telefono',
                  'usuario', 'contrasena', 'ciudadnombre']
        extra_kwargs = {'contrasena': {'write_only': True, 'required': True}}


class ciudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudad
        fields = ['id', 'nombre']
        
class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ['id', 'nombre']



class productoSerializer (serializers.ModelSerializer):   
    categoria=serializers.CharField(
        source='categoria.nombre',
        read_only=True
    )
    
    class Meta:
        model = producto
        fields = ['nombre', 'categoria','activo','precio']
        
        
class GrupoyModificacionSerializer(serializers.ModelSerializer):
    
    nombreModificacion=serializers.CharField(
        source='modificador.nombre',
        read_only=True
    )       
    class Meta:
        model = unionModificacion
        fields = ['id','grupoModificador','nombreModificacion']
    
        
class grupo_modificaSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = grupo_modifica
        fields = ['id','nombre']

class conexionProductoSerializer (serializers.ModelSerializer):
    productonombre=serializers.CharField(
        source='producto.nombre',
        read_only=True
    ) 
    productoprecio=serializers.CharField(
        source='producto.precio',
        read_only=True
    )
    grupoModificador=serializers.CharField(
        source='grupoModificador.nombre',
        read_only=True
    )
    
    class Meta:
        model = conexionProducto
        fields = ['producto','productonombre','productoprecio','unionModificacion','grupoModificador']

     

        
