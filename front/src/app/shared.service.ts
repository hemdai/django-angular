import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = "http://127.0.0.1:8000/api";
  readonly PhotoUrl = "http://127.0.0.1:8000/media";

  constructor(private http: HttpClient) { }
  
  getDepList(): Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/department/');
  }

  addDepartment(val: any) {
    return this.http.post(this.APIUrl + '/department/', val);
  }

  updateDepartment(val: any, numb:0) {
    return this.http.put(this.APIUrl + '/department/' + val, numb);
  }

  deleteDepartment(val: any) {
    return this.http.delete(this.APIUrl+'/depeartment/'+val)
  }

  getEmplist(): Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employee/');
  }

  addEmployee(val: any) {
    return this.http.post(this.APIUrl + '/employee/', val);
  }

  updateEmployee(val: any, numb:0) {
    return this.http.put(this.APIUrl + '/employee/' + val, numb);
  }

  deleteEmployee(val: any) {
    return this.http.delete(this.APIUrl+'/employee/'+val)
  }

  uploadPhoto(val: any) {
    return this.http.post(this.APIUrl + '/SaveFile', val);
  }
  

}
