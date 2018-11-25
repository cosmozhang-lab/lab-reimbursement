import { Injectable } from '@angular/core';

export interface User {
  username: string;
  nickname: string;
  token?: string;
  [other: string]: any
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  public user: User | undefined;
  public token: string | undefined;

  constructor() {
    var userjson = window.localStorage.getItem("login_user");
    if (userjson) {
      this.user = JSON.parse(userjson);
      this.token = this.user.token;
    } else {
      this.user = undefined;
      this.token = undefined;
    }
  }

  setLogin (user: User, token: string | undefined) {
    if (token) user.token = token;
    window.localStorage.setItem("login_user", JSON.stringify(user));
    this.user = user;
    this.token = user.token;
  }

  clearLogin () {
    window.localStorage.removeItem("login_user");
    this.user = undefined;
    this.token = undefined;
  }
}
