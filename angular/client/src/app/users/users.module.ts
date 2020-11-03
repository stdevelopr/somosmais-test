import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListComponent } from './list/list.component';
import { FilterComponent } from './filter/filter.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { MatCardModule } from '@angular/material/card';
import { MatRadioModule } from '@angular/material/radio';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [ListComponent, FilterComponent],
  imports: [
    CommonModule,
    NgbModule,
    MatCardModule,
    MatRadioModule,
    BrowserAnimationsModule,
    FormsModule
  ],
  exports: [ListComponent, FilterComponent]
})
export class UsersModule {}
