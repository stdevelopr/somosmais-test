import { Component, OnInit } from '@angular/core';
import { UsersService } from 'src/app/users.service';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {
  constructor(private service: UsersService) {}

  user = {};
  ngOnInit(): void {
    this.user = this.service.getSelected();
  }
}
