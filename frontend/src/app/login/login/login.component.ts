import { Component, OnInit } from '@angular/core';
import { NavbarService } from "src/app/widgets/navbar/navbar.service";
import { BreadcrumbService } from "src/app/widgets/breadcrumb/breadcrumb.service";
import { HttpService, ApiResponse } from 'src/app/common/http.service';
import { LoginService, User } from 'src/app/common/login.service';
// import { window } from 'src/app/common/window';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  private username: string;
  private password: string;

  constructor(
    private navbar: NavbarService,
    private breadcrumb: BreadcrumbService,
    private http: HttpService,
    private service: LoginService
    ) { }

  ngOnInit() {
    // this.navbar.hide();
    this.breadcrumb.clear();
    this.username = "";
    this.password = "";
  }

  login () {
    this.service.login(this.username, this.password).subscribe((res) => {
      // if (res.success) {
      //   window.alert("Login success");
      // } else {
      //   window.alert("Login failed because " + res.reason);
      // }
    });
  }

  get formValid(): boolean {
    if (!this.username) return false;
    if (!this.password) return false;
    return true;
  }

}
