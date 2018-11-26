import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { AuthService } from "./auth.service";
import { extend, AnyData } from './utils';

interface HttpOptions {
    body?: any;
    headers?: HttpHeaders | {
        [header: string]: string | string[];
    };
    observe?: 'body';
    params?: HttpParams | {
        [param: string]: string | string[];
    };
    reportProgress?: boolean;
    responseType?: 'json';
    withCredentials?: boolean;
}

export interface ApiResponse<T=any> {
  success: boolean;
  reason?: string;
  data?: T;
}

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(
    private http: HttpClient,
    private auth: AuthService
    ) { }

  make_url(path: string) {
    return environment.apiroot + path;
  }

  get default_http_options() {
    let default_options = {
      headers: {},
      observe: 'body',
      responseType: "json"
    };
    let token = this.auth.token;
    if (token) default_options.headers["Authorization"] = token;
    return default_options;
  }

  make_options(...options_array: HttpOptions[]): HttpOptions {
    return this.extend_options.apply(undefined, [{}, this.default_http_options].concat(options_array));
  }
  extend_options(first_option: HttpOptions, ...other_options_array: HttpOptions[]): HttpOptions {
    for (let other_options of other_options_array) {
      if (other_options) {
        if (other_options.body !== undefined) first_option.body = other_options.body;
        if (other_options.headers !== undefined) first_option.headers = extend(first_option.headers || {}, other_options.headers);
        if (other_options.params !== undefined) first_option.params = extend(first_option.params || {}, other_options.params);
        if (other_options.reportProgress !== undefined) first_option.reportProgress = other_options.reportProgress;
        if (other_options.responseType !== undefined) first_option.responseType = other_options.responseType;
        if (other_options.withCredentials !== undefined) first_option.withCredentials = other_options.withCredentials;
      }
    }
    return first_option;
  }

  request<T=any> (method: string, path: string, options?: HttpOptions): Observable<T> {
    let url = this.make_url(path);
    let httpoptions = this.make_options(options);
    return this.http.request<T>(method, url, httpoptions);
  }

  get<T=any> (path: string, params?: AnyData, options?: HttpOptions): Observable<T> {
    let default_options: HttpOptions = {};
    if (params) default_options.params = params;
    return this.request<T>("GET", path, this.extend_options(default_options, options));
  }

  post<T=any> (path: string, body?: AnyData, options?: HttpOptions): Observable<T> {
    let default_options: HttpOptions = {};
    if (body) {
      // default_options.body = JSON.stringify(body);
      default_options.body = body;
      default_options.headers = { "Content-Type": "application/json" }
    }
    return this.request<T>("POST", path, this.extend_options(default_options, options));
  }
}
