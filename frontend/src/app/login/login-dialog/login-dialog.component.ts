import { Component, OnInit } from '@angular/core';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-login-dialog',
  templateUrl: './login-dialog.component.html',
  styleUrls: ['./login-dialog.component.scss']
})
export class LoginDialogComponent implements OnInit {

  private username: string;
  private password: string;

  constructor(
    private service: LoginService
    ) { }

  ngOnInit() {
    this.username = "";
    this.password = "";
  }

  close() {
  }

  login() {
    this.service.login(this.username, this.password).subscribe((res) => {
      if (res.success) {
      } else {
      }
    });
  }

  get valid(): boolean {
    if (!this.username) return false;
    if (!this.password) return false;
    return true;
  }

}
