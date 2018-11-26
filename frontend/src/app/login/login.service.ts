import { Injectable } from '@angular/core';
import { AuthService, User } from 'src/app/common/auth.service';
import { HttpService, ApiResponse } from 'src/app/common/http.service';
import { Observable, Observer } from 'rxjs';
import { map as rxmap } from 'rxjs/operators';

export { User } from 'src/app/common/auth.service';

export interface LoginData {
  user: User;
  token: string;
}

const reason_translate = {
  "user-not-exist": "此用户不存在",
  "incorrect-password": "密码错误",
  "not-login": "用户尚未登录"
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
    return this.http.post<ApiResponse<LoginData>>("/auth/login", {
      username: username,
      password: password
    }).pipe<ApiResponse<LoginData>>(rxmap((res) => {
      if (res.success) {
        this.store.setLogin(res.data.user, res.data.token);
      } else {
        res.reason = reason_translate[res.reason];
      }
      return res;
    }));
  }

  logout (): Observable<ApiResponse<void>> {
    let ob: Observable<ApiResponse<void>>;
    if (this.store.token) {
      ob = this.http.post<ApiResponse<void>>("/auth/logout").pipe(rxmap((res) => {
        if (res.success) {
          this.store.clearLogin();
        } else {
          res.reason = reason_translate[res.reason];
        }
        return res;
      }));
    } else {
      ob = Observable.create((observer: Observer<ApiResponse<void>>) => {
        observer.next({
          success: false,
          reason: reason_translate["not-login"]
        });
      });
    }
    return ob;
  }
}
