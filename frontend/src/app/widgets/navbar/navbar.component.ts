import { Component, OnInit } from '@angular/core';
import { NavbarService } from './navbar.service';
import { AuthService } from 'src/app/common/auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  constructor(
    private service: NavbarService,
    private auth: AuthService
    ) { }

  ngOnInit() {
  }

}
