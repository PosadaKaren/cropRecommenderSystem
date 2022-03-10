import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  private url = 'http://localhost:8000/plantainApp'

  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});

  constructor(private http: HttpClient) { }

  postCropUser(crop : any){
    return this.http.post<any>(`${this.url}/usercrops`, crop, {headers : this.httpHeaders})
  }

  getAllCropUser(){
    return this.http.get<any>(`${this.url}/userCrop`, {headers : this.httpHeaders})
  }

  getAllCrops(){
    return this.http.get<any>(`${this.url}/crops`, {headers : this.httpHeaders})
  }

}
