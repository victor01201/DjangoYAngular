import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Producto } from '../interfaces/producto';

@Injectable({
  providedIn: 'root'
})
export class ProductosService {
  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });


  productos: Producto[] = [
    {
      id: 1,
      nombre: "Pizza",
      descripcion: "Pizza con carne",
      precio: 500,
      imagen: "https://www.clara.es/medio/2019/05/22/comidas-rapidas-ensalada-de-atun-huevo-cocido_c3182eba_1000x1500.jpg"
    },
    {
      id: 2,
      nombre: "Pizza",
      descripcion: "Pizza con pollo",
      precio: 1500,
      imagen: "https://www.clara.es/medio/2019/05/22/comidas-rapidas-ensalada-de-atun-huevo-cocido_c3182eba_1000x1500.jpg"
    },
    {
      id: 3,
      nombre: "Pizza",
      descripcion: "Pizza con piña",
      precio: 2000,
      imagen: "https://www.clara.es/medio/2019/05/22/comidas-rapidas-ensalada-de-atun-huevo-cocido_c3182eba_1000x1500.jpg"
    },
    {
      id: 4,
      nombre: "Pizza",
      descripcion: "Pizza con jamon",
      precio: 2500,
      imagen: "https://www.clara.es/medio/2019/05/22/comidas-rapidas-ensalada-de-atun-huevo-cocido_c3182eba_1000x1500.jpg"
    },
    {
      id: 5,
      nombre: "Pizza",
      descripcion: "Pizza con champiñon",
      precio: 3000,
      imagen: "https://www.clara.es/medio/2019/05/22/comidas-rapidas-ensalada-de-atun-huevo-cocido_c3182eba_1000x1500.jpg"
    },
    {
      id: 6,
      nombre: "Pizza",
      descripcion: "Pizza vegana",
      precio: 3500,
      imagen: "https://www.clara.es/medio/2019/05/22/comidas-rapidas-ensalada-de-atun-huevo-cocido_c3182eba_1000x1500.jpg"
    },
    {
      id: 7,
      nombre: "Papas",
      descripcion: "Papas a la francesa",
      precio: 4000,
      imagen: "https://www.clara.es/medio/2019/05/22/comidas-rapidas-ensalada-de-atun-huevo-cocido_c3182eba_1000x1500.jpg"
    }
  ]

  constructor(private http: HttpClient) { }

  getproductos(): Producto[] {
    return this.productos;
  }
  getTodosProductos(): Observable<Producto[]> {
    return this.http.get<Producto[]>(this.baseurl + '/producto/',
      { headers: this.httpHeaders });
  }
}
