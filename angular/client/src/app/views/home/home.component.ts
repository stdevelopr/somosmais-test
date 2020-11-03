import { Component, OnInit } from '@angular/core';
import { UsersService } from 'src/app/users.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  title = 'App Client';
  region;
  type;
  pageNumber;
  pageSize;
  _data;

  constructor(private userService: UsersService) {}

  get data() {
    return this._data;
  }

  set data(data) {
    this._data = data;
  }

  ngOnInit() {
    this.pageSize = this.userService.getPageSize();
    this.pageNumber = this.userService.getPageNumber();
    this.region = this.userService.getRegion();
    this.userService
      .getUsers(this.region, this.type, this.pageSize, this.pageNumber)
      .subscribe(data => {
        this._data = data;
      });
  }

  onFilterRegion(region) {
    this.region = region;
    this.pageNumber = 1;
    this.userService.setRegion(region);
    this.userService
      .getUsers(
        this.region,
        this.type,
        this.userService.getPageSize(),
        this.pageNumber
      )
      .subscribe(data => {
        this._data = data;
      });
  }

  onFilterType(type) {
    this.type = type;
    this.pageNumber = 1;
    this.userService.setType(type);
    this.userService
      .getUsers(
        this.region,
        this.type,
        this.userService.getPageSize(),
        this.pageNumber
      )
      .subscribe(data => {
        this.data = data;
      });
  }

  pageChange(page) {
    this.userService.setPageNumber(page);
    this.userService
      .getUsers(this.region, this.type, this.userService.getPageSize(), page)
      .subscribe(data => {
        this._data = data;
      });
  }

  pageSizeChange(pageSize) {
    this.pageSize = pageSize;
    this.userService.setPageSize(pageSize);
    this.userService
      .getUsers(
        this.region,
        this.type,
        pageSize,
        this.userService.getPageNumber()
      )
      .subscribe(data => {
        this._data = data;
      });
  }
}
