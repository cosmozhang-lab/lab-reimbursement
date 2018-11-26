import { Injectable, Component, OnInit, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BsModalService, BsModalRef } from 'ngx-bootstrap/modal';
import { Observable, Observer } from 'rxjs';
import { extend } from 'src/app/common/utils';


export interface MessageBoxResult {
}

interface DialogOptions {
  type?: string;
  title?: string;
  content?: string;
}

function make_config(options?: DialogOptions): DialogOptions;
function make_config(content: string, options?: DialogOptions): DialogOptions;
function make_config(title: string, content?: string, options?: DialogOptions): DialogOptions;
function make_config(...args: any[]): DialogOptions {
  let title: string = undefined;
  let content: string = undefined;
  let options: DialogOptions = undefined;
  for (let argitem of args) {
    if (typeof argitem === "string") {
      if (title === undefined) title = argitem;
      else if (content === undefined) title = argitem;
    } else if (typeof argitem === "object") {
      options = extend({}, argitem);
      break;
    }
  }
  if (title) options.title = title;
  if (content) options.content = content;
  return options;
}

@Injectable({
  providedIn: 'root'
})
export class DialogService {
  constructor(
    private modalService: BsModalService) {}

  show(options: DialogOptions): Observable<any> {
    let modalService = this.modalService;
    let modelRef = modalService.show(DialogComponent, {initialState: options});
    let modelComponent: DialogComponent = modelRef.content;
    return Observable.create(function(observer: Observer<any>) {
      modelComponent.onClose.subscribe((res) => {
        observer.next(res);
      });
    });
  }

  message(type:string, ...args: any[]): Observable<MessageBoxResult> {
    let title: string = undefined;
    let content: string = undefined;
    let options: DialogOptions = {};
    for (let argitem of args) {
      if (typeof argitem === "string") {
        if (title === undefined) title = argitem;
        else if (content === undefined) content = argitem;
      } else if (typeof argitem === "object") {
        options = extend(options, argitem);
        break;
      }
    }
    if (title) options.title = title;
    if (content) options.content = content;
    options.type = type;
    return this.show(options);
  }

  info(options?: DialogOptions): Observable<MessageBoxResult>;
  info(content: string, options?: DialogOptions): Observable<MessageBoxResult>;
  info(title: string, content?: string, options?: DialogOptions): Observable<MessageBoxResult>;
  info(...args: any[]): Observable<MessageBoxResult> {
    return this.message.apply(this, ["info"].concat(args));
  }

  warning(options?: DialogOptions): Observable<MessageBoxResult>;
  warning(content: string, options?: DialogOptions): Observable<MessageBoxResult>;
  warning(title: string, content?: string, options?: DialogOptions): Observable<MessageBoxResult>;
  warning(...args: any[]): Observable<MessageBoxResult> {
    return this.message.apply(this, ["warning"].concat(args));
  }

  error(options?: DialogOptions): Observable<MessageBoxResult>;
  error(content: string, options?: DialogOptions): Observable<MessageBoxResult>;
  error(title: string, content?: string, options?: DialogOptions): Observable<MessageBoxResult>;
  error(...args: any[]): Observable<MessageBoxResult> {
    return this.message.apply(this, ["error"].concat(args));
  }

}

@Component({
  selector: 'app-dialog',
  templateUrl: './dialog.component.html',
  styleUrls: ['./dialog.component.scss']
})
export class DialogComponent implements OnInit {

  private type: string = "info";
  private title: string;
  private content: string;

  onClose: EventEmitter<any> = new EventEmitter<any>();

  constructor(public ref: BsModalRef) { }

  ngOnInit() {
  }

  set config(options: DialogOptions) {
    const default_titles = {
      info: "提示",
      warning: "警告",
      error: "出错了",
      question: "请问"
    };
    this.type = options.type || "info";
    this.title = options.title || default_titles[this.type];
    this.content = options.content || "";
  }
  get config() {
    return {
      type: this.type,
      title: this.title,
      content: this.content
    };
  }

  get clsname(): string {
    const types2classnames = {
      info: "info",
      warning: "warning",
      error: "danger",
      question: "primary"
    }
    return types2classnames[this.type];
  }

  close() {
    this.ref.hide();
    this.onClose.emit();
  }
}
