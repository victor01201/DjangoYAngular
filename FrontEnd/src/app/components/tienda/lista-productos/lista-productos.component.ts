import { Component, OnInit } from '@angular/core';
import { Producto } from 'src/app/interfaces/producto';
import { ProductosService } from 'src/app/services/productos.service';

@Component({
  selector: 'app-lista-productos',
  templateUrl: './lista-productos.component.html',
  styleUrls: ['./lista-productos.component.css']
})
export class ListaProductosComponent implements OnInit {

  listaProductos: Producto[]= [];

  constructor(private _productoservices:ProductosService) { }

  ngOnInit(): void {    
    this.listarproductos();
    console.log(this.listaProductos[0])
  }

  listarproductos(){
    this.listaProductos = this._productoservices.getproductos();

   /*  this._productoservices.getTodosProductos().subscribe((data:Producto[])=>{
      this.listaProductos = data;
    }); */
  }


}
