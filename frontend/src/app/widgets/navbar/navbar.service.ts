import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class NavbarService {
  private hidden: boolean;
  constructor() {
    this.hidden = false;
  }

  show() {
    this.hidden = false;
  }

  hide() {
    this.hidden = true;
  }
}
