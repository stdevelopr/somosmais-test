import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from '../environments/environment';

interface UserResponse {
  users: [];
  totalCount: number;
}

@Injectable({
  providedIn: 'root'
})
export class UsersService {
  constructor(private http: HttpClient) {}

  private selectedUser;
  private _pageSize = '10';
  private _pageNumber = '1';
  private _region = 'all';
  private _type = 'all';
  serverURL = environment.serverURL;

  getUsers(
    region,
    type,
    pageSize = this._pageSize,
    pageNumber = this._pageNumber
  ) {
    const httpParams = new HttpParams({
      fromObject: {
        pageSize: pageSize,
        pageNumber: pageNumber,
        region: region ? region : this._region,
        type: type ? type : this._type
      }
    });
    return this.http.get<UserResponse>(this.serverURL + '/clients', {
      params: httpParams
    });
  }

  getSelected() {
    return this.selectedUser;
  }

  setSelected(user) {
    this.selectedUser = user;
  }

  getPageSize() {
    return this._pageSize;
  }

  setPageSize(pageSize) {
    this._pageSize = pageSize;
  }

  getPageNumber() {
    return this._pageNumber;
  }

  setPageNumber(pageNumber) {
    this._pageNumber = pageNumber;
  }

  getRegion() {
    return this._region;
  }

  setRegion(region) {
    this._region = region;
  }

  getType() {
    return this._type;
  }

  setType(type) {
    this._type = type;
  }
}
