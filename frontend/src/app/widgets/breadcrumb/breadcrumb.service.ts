import { Injectable } from '@angular/core';

export interface BreadcrumbItem {
  name: string,
  link: string
}

@Injectable({
  providedIn: 'root'
})
export class BreadcrumbService {
  private hidden: boolean;
  private items: BreadcrumbItem[] = [];
  constructor() {
    this.hidden = false;
  }
  show() {
    this.hidden = false;
  }
  hide() {
    this.hidden = true;
  }
  update(items: BreadcrumbItem[]) {
    this.items = items;
  }
  push(item: BreadcrumbItem) {
    this.items = [].concat(this.items, [item]);
  }
  pop() {
    this.items = this.items.slice(0, this.items.length-1);
  }
  clear() {
    this.items = [];
  }
}
