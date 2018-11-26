import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { ModalModule as BsModalModule } from 'ngx-bootstrap/modal';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './widgets/navbar/navbar.component';
import { BreadcrumbComponent } from './widgets/breadcrumb/breadcrumb.component';
import { DialogModule } from './widgets/dialog/dialog.module';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    BreadcrumbComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    BsModalModule.forRoot(),
    AppRoutingModule,
    DialogModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
