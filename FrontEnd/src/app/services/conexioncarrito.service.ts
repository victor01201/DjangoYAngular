import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { Producto } from '../interfaces/producto';

@Injectable({
  providedIn: 'root'
})
export class ConexioncarritoService {

  subject = new Subject()

  constructor() { }

  enviarproducto(producto:Producto){
    this.subject.next(producto)
  }

  getproducto(): Observable<any>{
    return this.subject.asObservable();
  }
}
