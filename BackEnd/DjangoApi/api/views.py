from rest_framework import viewsets
from rest_framework.response import Response
from DjangoApi.api.serializers import *
from .models import *



class tarjetaViewSet(viewsets.ModelViewSet):
    queryset = tarjeta.objects.all()
    serializer_class = tarjetaSerializer
    
    
class ciudadViewSet(viewsets.ModelViewSet):
    queryset = ciudad.objects.all()
    serializer_class = ciudadSerializer        
    
class personaViewSet(viewsets.ModelViewSet):
    queryset = persona.objects.all()
    serializer_class = personaSerializer  
    
class categoriaViewSet(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer  
    
class productoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = productoSerializer
    
class GrupoyModificacionViewSet(viewsets.ModelViewSet):
    queryset = unionModificacion.objects.all()
    serializer_class = GrupoyModificacionSerializer
    
class grupo_modificaViewSet(viewsets.ModelViewSet):
    queryset = grupo_modifica.objects.all()
    serializer_class = grupo_modificaSerializer
    
class conexionProductoViewSet(viewsets.ModelViewSet):
    queryset = conexionProducto.objects.all()
    serializer_class = conexionProductoSerializer  
