import { Injectable } from '@angular/core';
import { AuthService, User } from './auth.service';
import { HttpService, ApiResponse } from './http.service';
import { Observable, Observer } from 'rxjs';

export { User } from './auth.service';

export interface LoginData {
  user: User;
  token: string;
}

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(
    private store: AuthService,
    private http: HttpService
    ) {
  }

  login (username: string, password: string): Observable<ApiResponse<LoginData>> {
    let ob: Observable<ApiResponse<LoginData>> = Observable.create((observer: Observer<ApiResponse<LoginData>>) => {
      this.http.post<ApiResponse<LoginData>>("/auth/login", {
        username: username,
        password: password
      }).subscribe((res) => {
        if (res.success) {
          this.store.setLogin(res.data.user, res.data.token);
        }
        observer.next(res);
      });
    });
    return ob;
  }
}
