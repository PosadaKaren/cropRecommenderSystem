import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrincipalComponent } from './pages/principal/principal.component';

const routes: Routes = [
  {
    path : '',
    redirectTo : 'principal',
    pathMatch : 'full'
  },
  {
    path : 'principal',
    //loadChildren: () => import('./pages/principal/principal.module').then(m => m.PrincipalModule)
    component : PrincipalComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
