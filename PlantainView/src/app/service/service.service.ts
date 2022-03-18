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

  createListObj(list : any){
    let newList : any[] = []
    for (const i in list){
      const obj = {
        fosforo : list[i][0],
        aluminio : list[i][1],
        calcio : list[i][2],
        potasio : list[i][3],
        sodio : list[i][4],
        zinc : list[i][5],
        pearson : list[i][6],
      }
      newList.push(obj)
    }
    return newList
  }

  type(list: any){
    var temp = list.shift()
    const max = Math.max(list)
    const type = list.indexOf(max,0)

    if (type == 0){
      return 'Dominico-harton'
    } else if (type == 1){
      return 'Harton'
    } else {
      return 'Dominico'
    }
  }

}
