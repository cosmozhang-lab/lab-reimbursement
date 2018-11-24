import { Component, OnInit } from '@angular/core';
import { BreadcrumbService } from './widgets/breadcrumb/breadcrumb.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  private title = 'labreimbursement-fe';
  constructor(
    private breadcrumb: BreadcrumbService) {
  }

  ngOnInit() {
    this.breadcrumb.push({ name: "首页", link: "/" });
    this.breadcrumb.push({ name: "控制台", link: "/" });
  }
}
