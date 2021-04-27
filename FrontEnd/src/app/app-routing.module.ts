import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioComponent } from './components/estatico/inicio/inicio.component';
import { SeleccionComponent } from './components/tienda/seleccion/seleccion.component';


const routes: Routes = [
  {
    path:"", redirectTo: 'inicio', pathMatch: 'full'
  },
  {
    path:"inicio" ,  component: InicioComponent
  },
  {
    path:"tienda" ,  component: SeleccionComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
