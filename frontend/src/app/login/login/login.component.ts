import { Component, OnInit } from '@angular/core';
import { NavbarService } from "src/app/widgets/navbar/navbar.service";
import { BreadcrumbService } from "src/app/widgets/breadcrumb/breadcrumb.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(
    private navbar: NavbarService,
    private breadcrumb: BreadcrumbService
    ) { }

  ngOnInit() {
    // this.navbar.hide();
    this.breadcrumb.clear();
    console.log(this.navbar);
  }

}
