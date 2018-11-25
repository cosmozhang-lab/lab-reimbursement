import { Injectable } from '@angular/core';
import { AuthService } from 'src/app/common/auth.service';

@Injectable({
  providedIn: 'root'
})
export class NavbarService {
  private hidden: boolean;
  constructor(
    private auth: AuthService
    ) {
    this.hidden = false;
  }

  show() {
    this.hidden = false;
  }

  hide() {
    this.hidden = true;
  }
}
