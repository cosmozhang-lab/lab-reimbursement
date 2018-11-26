import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DialogComponent } from './dialog.service';

@NgModule({
  declarations: [DialogComponent],
  imports: [
    CommonModule
  ],
  entryComponents: [DialogComponent]
})
export class DialogModule {
  constructor() {}
}
