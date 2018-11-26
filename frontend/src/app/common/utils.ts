export interface AnyData {
  [key: string]: any;
}

export function extend (deep: boolean, first: AnyData, ...others: AnyData[]): AnyData;
export function extend (first: AnyData, ...others: AnyData[]): AnyData;
export function extend (...args: any[]): AnyData {
  let deep: boolean = false;
  if (typeof args[0] === "boolean") {
    deep = args[0];
    args = args.slice(1);
  }
  let first: AnyData = args[0] || {};
  let others: AnyData[] = args.slice(1);
  for (let otheritem of others) {
    if (otheritem) {
      for (let k in otheritem) {
        if (deep && typeof first[k] === "object") {
          extend(true, first[k], otheritem[k]);
        } else {
          first[k] = otheritem[k];
        }
      }
    }
  }
  return first;
}
