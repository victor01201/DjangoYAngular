import { Component, Input, OnInit } from '@angular/core';
import { Producto } from 'src/app/interfaces/producto';
import { ConexioncarritoService } from 'src/app/services/conexioncarrito.service';

@Component({
  selector: 'app-producto',
  templateUrl: './producto.component.html',
  styleUrls: ['./producto.component.css']
})
export class ProductoComponent implements OnInit {

  @Input() productoitem: Producto =
    {
      id: 0,
      nombre: "",
      descripcion: "",
      precio: 0,
      imagen: ""
    };

  constructor(private _conexionservices: ConexioncarritoService) { }

  ngOnInit(): void {
  }

  agregarproducto(){
    this._conexionservices.enviarproducto(this.productoitem);
  }

}
