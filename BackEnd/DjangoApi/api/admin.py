from django.contrib import admin
from .models import *

admin.site.register(producto)
admin.site.register(categoria)
admin.site.register(modificador)
admin.site.register(unionModificacion)
admin.site.register(conexionProducto)

admin.site.register(grupo_modifica)


admin.site.register(tarjeta)
admin.site.register(ciudad)
admin.site.register(persona)

admin.site.register(sucursal)
admin.site.register(admincontent)

admin.site.register(sucursalproducto)

admin.site.register(ordenestempo)
admin.site.register(ordeneshistorial)


admin.site.register(ordentemp)
admin.site.register(ordenhistorial)
