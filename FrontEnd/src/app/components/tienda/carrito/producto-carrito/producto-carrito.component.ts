import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-producto-carrito',
  templateUrl: './producto-carrito.component.html',
  styleUrls: ['./producto-carrito.component.css']
})
export class ProductoCarritoComponent implements OnInit {

  @Input() carroitem:any={}

  constructor() { }

  ngOnInit(): void {
  }

}
