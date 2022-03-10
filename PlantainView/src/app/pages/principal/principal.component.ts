import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';

import { ServiceService } from 'src/app/service/service.service';

@Component({
  selector: 'app-principal',
  templateUrl: './principal.component.html',
  styleUrls: ['./principal.component.scss'],
})
export class PrincipalComponent implements OnInit {


  similarity : string = '';
  cropToRecommender : FormGroup;

  constructor(private fb : FormBuilder, private cropService : ServiceService, private _snackBar : MatSnackBar ) {
    this.cropToRecommender = fb.group({
      fosforo : ['', Validators.required],
      aluminio : ['', Validators.required],
      calcio : ['', Validators.required],
      potasio : ['', Validators.required],
      sodio : ['', Validators.required],
      zinc : ['', Validators.required]
    })
  }

  ngOnInit(): void {}

  sendCrop(){
    const cropTosend = {
      fosforo : this.cropToRecommender.value.fosforo,
      aluminio : this.cropToRecommender.value.aluminio,
      calcio : this.cropToRecommender.value.calcio,
      potasio : this.cropToRecommender.value.potasio,
      sodio : this.cropToRecommender.value.sodio,
      zinc : this.cropToRecommender.value.zinc
    }
    this.cropService.postCropUser(cropTosend)
    .subscribe((data) => {
      this._snackBar.open('el cultivo se proceso correctamente', 'Ok', {duration : 2000, panelClass: ['green-plantain']})
      this.similarity = data.similarity
    }, (err) => {
      this._snackBar.open('Al parecer ocurrio un problema', 'Ok', {duration : 2000, panelClass: ['red-warning']})
    })
  }

}
