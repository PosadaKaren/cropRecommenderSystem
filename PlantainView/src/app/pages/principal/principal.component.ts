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


  similarity : string = ''
  recomendedType : string = ''
  isPosible : boolean = false;
  mostSimilarCrops : any[] = [];
  cropToRecommender : FormGroup;

  constructor(private fb : FormBuilder, private cropService : ServiceService, private _snackBar : MatSnackBar ) {
    this.cropToRecommender = fb.group({
      ph : ['', Validators.required],
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
      fosforo : parseFloat(this.cropToRecommender.value.fosforo),
      aluminio : parseFloat(this.cropToRecommender.value.aluminio),
      calcio : parseFloat(this.cropToRecommender.value.calcio),
      potasio : parseFloat(this.cropToRecommender.value.potasio),
      sodio : parseFloat(this.cropToRecommender.value.sodio),
      zinc : parseFloat(this.cropToRecommender.value.zinc)
    }
    this.cropService.postCropUser(cropTosend)
    .subscribe((data) => {
      this.mostSimilarCrops = this.cropService.createListObj(data.document)

      this._snackBar.open('el cultivo se proceso correctamente', 'Ok', {duration : 2000, panelClass: ['green-plantain']})
      const number = data.similarity

      let simStrig = number.toFixed(4).toString()
      this.similarity = simStrig;
      this.posibility(this.similarity);
      this.recomendedType = this.cropService.type(data.type)

    }, (err) => {
      this._snackBar.open('Al parecer ocurrio un problema', 'Ok', {duration : 2000, panelClass: ['red-warning']})
    })
  }

  posibility(similarity : string){
    const sim = parseInt(similarity)
    console.log(sim)
    if(sim > 0.6){
      this.isPosible = true
    } else {
      this.isPosible= false
    }
  }

}
