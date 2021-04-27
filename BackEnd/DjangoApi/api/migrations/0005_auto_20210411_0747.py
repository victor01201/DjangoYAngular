# Generated by Django 3.1.7 on 2021-04-11 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210411_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='adicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='modificador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ordeneshistorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entregado', models.BooleanField(null=True, verbose_name=django.db.models.deletion.SET_NULL)),
                ('razon', models.CharField(max_length=30, null=True)),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('fechaentrega', models.DateField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ordenestempo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entregado', models.BooleanField(null=True, verbose_name=django.db.models.deletion.SET_NULL)),
                ('razon', models.CharField(max_length=30, null=True)),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('fechaentrega', models.DateField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('activo', models.BooleanField()),
                ('numeroTarjeta', models.IntegerField()),
                ('adicion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nombreAdicion', to='api.adicion')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nombreCategoria', to='api.categoria')),
                ('modificador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nombreModificador', to='api.modificador')),
            ],
        ),
        migrations.CreateModel(
            name='sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sucursalCiudad', to='api.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='sucursalproducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sucursalproductoProducto', to='api.producto')),
                ('sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sucursalproductoSucursal', to='api.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=30)),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personaCiudad', to='api.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='ordentemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordenid', to='api.ordenestempo')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nombreProducto', to='api.producto')),
            ],
        ),
        migrations.CreateModel(
            name='ordenhistorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordenhistorialordenid', to='api.ordeneshistorial')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordenhistorialProducto', to='api.producto')),
            ],
        ),
        migrations.AddField(
            model_name='ordenestempo',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personaid', to='api.persona'),
        ),
        migrations.AddField(
            model_name='ordeneshistorial',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordeneshistorialid', to='api.persona'),
        ),
        migrations.CreateModel(
            name='admincontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=30)),
                ('sucursalNombre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nombreSucursal', to='api.sucursal')),
            ],
        ),
    ]
