import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/estatico/header/header.component';
import { FooterComponent } from './components/estatico/footer/footer.component';
import { NavbarComponent } from './components/estatico/navbar/navbar.component';
import { CarritoComponent } from './components/tienda/carrito/carrito.component';
import { ListaProductosComponent } from './components/tienda/lista-productos/lista-productos.component';
import { SeleccionComponent } from './components/tienda/seleccion/seleccion.component';
import { ProductoComponent } from './components/tienda/lista-productos/producto/producto.component';
import { ProductoCarritoComponent } from './components/tienda/carrito/producto-carrito/producto-carrito.component';
import { InicioComponent } from './components/estatico/inicio/inicio.component';
import { HeaderinicioComponent } from './components/estatico/inicio/headerinicio/headerinicio.component';
import { SeccionComponent } from './components/estatico/inicio/seccion/seccion.component';
import { CategoriaComponent } from './components/estatico/inicio/categoria/categoria.component';
import { ChefsComponent } from './components/estatico/inicio/chefs/chefs.component';
import { CompraComponent } from './components/compra/compra.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    NavbarComponent,
    CarritoComponent,
    ListaProductosComponent,
    SeleccionComponent,
    ProductoComponent,
    ProductoCarritoComponent,
    InicioComponent,
    HeaderinicioComponent,
    SeccionComponent,
    CategoriaComponent,
    ChefsComponent,
    CompraComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
