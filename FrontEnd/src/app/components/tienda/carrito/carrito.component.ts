import { Component, OnInit } from '@angular/core';
import { Producto } from 'src/app/interfaces/producto';
import { ConexioncarritoService } from 'src/app/services/conexioncarrito.service';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent implements OnInit {

  carroProductos: any[] = [];

  carroTotal = 0

  constructor(private _conexionservices: ConexioncarritoService) { }

  ngOnInit(): void {
    this.AgregarProductoCarro();
  }

  AgregarProductoCarro() {

    let productoexiste = false;

    this._conexionservices.getproducto().subscribe((producto: Producto) => {

      console.log(this.carroProductos)

      for (let i in this.carroProductos) {
        if (this.carroProductos[i].productoid === producto.id){
          this.carroProductos[i].cantidad++;
          productoexiste = true;
          break;
        }
        
      }
      

      if (!productoexiste) {
        this.carroProductos.push({
          productoid: producto.id,
          productonombre: producto.nombre,
          cantidad: 1,
          precio: producto.precio
        })
      }
      productoexiste=false;
      /* this.carroProductos.push({
        productonombre: producto.nombre,
        cantidad: 1,
        precio: producto.precio
      }); */

      this.carroTotal = 0;
      this.carroProductos.forEach(productoitem => {
        this.carroTotal += (productoitem.cantidad * productoitem.precio)
      })
      
    });
  }
}
