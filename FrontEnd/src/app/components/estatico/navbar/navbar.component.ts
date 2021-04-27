import { Component, OnInit } from '@angular/core';
import { CiudadService } from 'src/app/services/ciudad.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {



  ciudades:any[] = [    
    {
      "nombre": "Pereira"
    },
    {
      "nombre": "Manizales"
    },
    {
      "nombre": "Armenia"
    },
    {
      "nombre": "Bogota"
    },
    {
      "nombre": "Cali"
    },
    {
      "nombre": "Medellin"
    }
  ]

  ciudadtitulo=this.ciudades[0].nombre;

  constructor(private _ciudadServices: CiudadService) { }

  ngOnInit(): void {
    this.getciudad();
  }

  getciudad() {
    /* this._ciudadServices.getTodasCiudades().subscribe(data => {
      this.ciudadtitulo=this.ciudades[0].nombre;
      this.ciudades = data;
    }) */
  }

  seleccionciudad(nombre: string) {
    this.ciudadtitulo = nombre;
  }

}
