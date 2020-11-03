import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { UsersService } from 'src/app/users.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {
  constructor(private router: Router, private service: UsersService) {}

  private _users: any;

  get users(): any {
    return this._users;
  }
  @Input()
  set users(data: any) {
    this._users = data;
  }

  ngOnInit(): void {}

  showUser(user) {
    this.service.setSelected(user);
    this.router.navigate(['/details']);
  }
}
