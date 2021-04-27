from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from DjangoApi.api import views
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'tarjeta', views.tarjetaViewSet)
router.register(r'ciudad', views.ciudadViewSet)
router.register(r'persona', views.personaViewSet)
router.register(r'categoria', views.categoriaViewSet)
router.register(r'producto', views.productoViewSet)
router.register(r'GrupoyModificacion', views.GrupoyModificacionViewSet)
router.register(r'grupo_modifica', views.grupo_modificaViewSet)
router.register(r'conexionProducto', views.conexionProductoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'auth/', ObtainAuthToken.as_view)
]