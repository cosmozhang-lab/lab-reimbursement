import { Component, OnInit } from '@angular/core';
import { NavbarService } from './navbar.service';
import { AuthService } from 'src/app/common/auth.service';
import { LoginService } from 'src/app/login/login.service';
import * as $ from 'jquery';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  private showUserMenu: boolean = false;

  constructor(
    private service: NavbarService,
    private auth: AuthService,
    private login: LoginService
    ) { }

  ngOnInit() {
    $(document).on("click", () => {
      this.showUserMenu = false;
    });
  }

  onUserItemClick(event) {
    event.stopPropagation();
    this.showUserMenu = !this.showUserMenu;
  }

  userMenuLogout() {
    this.login.logout().subscribe();
  }

}
