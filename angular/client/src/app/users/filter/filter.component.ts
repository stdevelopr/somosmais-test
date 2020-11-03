import { Component, Output, EventEmitter } from '@angular/core';
import { UsersService } from '../../users.service';

@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.css']
})
export class FilterComponent {
  constructor(private userService: UsersService) {}
  private _region = 'all';
  private _type = 'all';

  ngOnInit() {
    this.region = this.userService.getRegion();
    this.type = this.userService.getType();
  }

  get region() {
    return this._region;
  }

  @Output('filterRegion') filterRegion: EventEmitter<any> = new EventEmitter();
  set region(region) {
    this._region = region;
    this.filterRegion.emit(this._region);
  }

  get type() {
    return this._type;
  }

  @Output('filterType') filterType: EventEmitter<any> = new EventEmitter();
  set type(type) {
    this._type = type;
    this.filterType.emit(this._type);
  }
}
