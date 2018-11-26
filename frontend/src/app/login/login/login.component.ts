import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NavbarService } from "src/app/widgets/navbar/navbar.service";
import { BreadcrumbService } from "src/app/widgets/breadcrumb/breadcrumb.service";
import { LoginService } from '../login.service';
import { DialogService } from 'src/app/widgets/dialog/dialog.service';

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
    private service: LoginService,
    private dialog: DialogService,
    private router: Router
    ) { }

  ngOnInit() {
    // this.navbar.hide();
    this.breadcrumb.clear();
    this.username = "";
    this.password = "";
  }

  login () {
    this.service.login(this.username, this.password).subscribe((res) => {
      if (res.success) {
        this.router.navigateByUrl("/");
      } else {
        this.dialog.error("登录失败", res.reason);
      }
    });
  }

  get formValid(): boolean {
    if (!this.username) return false;
    if (!this.password) return false;
    return true;
  }

}
