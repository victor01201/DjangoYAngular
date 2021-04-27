from django.db import models
from django.db.models.deletion import SET_NULL
from rest_framework.fields import set_value


class ciudad(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f'ciudad {self.id}: {self.nombre}'


class tarjeta(models.Model):
    titular = models.CharField(max_length=255)
    numeroTarjeta = models.IntegerField()
    fechaExpiracion = models.CharField(max_length=5)
    cvv = models.IntegerField()
    ciudad = models.ForeignKey(
        ciudad, related_name='nombreCiudad', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'tarjeta {self.id}: {self.titular} con numero de tarjeta {self.numeroTarjeta}'


class persona (models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    ciudad = models.ForeignKey(
        ciudad, related_name='personaCiudad', on_delete=models.SET_NULL, null=True)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)

    def __str__(self):
        return f'persona {self.id}: {self.nombre}'


class sucursal(models.Model):
    nombre = models.CharField(max_length=30)
    ciudad = models.ForeignKey(
        ciudad, related_name='sucursalCiudad', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'sucursal {self.id}: {self.nombre}'


class admincontent(models.Model):
    nombre = models.CharField(max_length=30)
    sucursalNombre = models.ForeignKey(
        sucursal, related_name="nombreSucursal", on_delete=models.SET_NULL, null=True)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)

    def __str__(self):
        return f'admin {self.id}: {self.nombre}'


class categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'categoria {self.id}: {self.nombre}'


class modificador(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'modificador {self.id}: {self.nombre}'


class grupo_modifica(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f' Grupo de Modificacion:  {self.id}: {self.nombre}'


class unionModificacion(models.Model):
    grupoModificador = models.ForeignKey(
        grupo_modifica, related_name="gruponombre", on_delete=models.SET_NULL, null=True)
    modificador = models.ForeignKey(
        modificador, related_name="modificadornombre", on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return f'modificacion {self.id}: {self.grupoModificador} {self.modificador}'


class producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.ForeignKey(
        categoria, related_name="nombreCategoria", on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField()
    precio = models.IntegerField()
    
    class Meta:
        unique_together = ['categoria']

    def __str__(self):
         return '%s: %d' % (self.nombre, self.precio)


class conexionProducto(models.Model):
    producto = models.ForeignKey(
        producto, related_name="productornombre", on_delete=models.SET_NULL, null=True)
    unionModificacion = models.ForeignKey(
        unionModificacion, related_name="nombreunion", on_delete=models.SET_NULL, null=True)
    class Meta:
        unique_together = ['producto', 'unionModificacion']        
        ordering = ['producto']
    
    

    def __str__(self):
        return f'producto {self.id}: {self.producto} {self.unionModificacion}'


class sucursalproducto(models.Model):
    sucursal = models.ForeignKey(
        sucursal, related_name="sucursalproductoSucursal", on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(
        producto, related_name="sucursalproductoProducto", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'sucursal {self.id}: {self.producto}'


class ordenestempo (models.Model):
    persona = models.ForeignKey(
        persona, related_name="personaid", on_delete=models.SET_NULL, null=True)
    entregado = models.BooleanField(SET_NULL, null=True)
    razon = models.CharField(max_length=30, null=True)
    fechacreacion = models.DateField(auto_now=True)
    fechaentrega = models.DateField(auto_now=False)
    total = models.IntegerField()

    def __str__(self):
        return f'ordenes {self.id}: {self.persona} {self.fechacreacion}'


class ordeneshistorial (models.Model):
    persona = models.ForeignKey(
        persona, related_name="ordeneshistorialid", on_delete=models.SET_NULL, null=True)
    entregado = models.BooleanField(SET_NULL, null=True)
    razon = models.CharField(max_length=30, null=True)
    fechacreacion = models.DateField(auto_now=True)
    fechaentrega = models.DateField(auto_now=False)
    total = models.IntegerField()

    def __str__(self):
        return f'ordenes {self.id}: {self.persona} {self.fechacreacion}'


class ordentemp (models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(
        producto, related_name="nombreProducto", on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(
        ordenestempo, related_name="ordenid", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'orden {self.id}: {self.cantidad} {self.producto}'


class ordenhistorial (models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(
        producto, related_name="ordenhistorialProducto", on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(
        ordeneshistorial, related_name="ordenhistorialordenid", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'orden {self.id}: {self.cantidad} {self.producto}'
