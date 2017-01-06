/**
 * Created by tspycher on 04.01.17.
 */
import 'rxjs/add/operator/map'
import {Http} from "@angular/http";


export class BugService {

  private baseurl:string;

  static get parameters() {
    return [[Http]];
  }

  constructor (private http:Http) {
      this.setBaseUrl("http://127.0.0.1:5000/");
  }

  setBaseUrl(url:string) {
      console.log(url);
      this.baseurl = url;
  }

  createUrl(url:string) {
    return this.baseurl + url;
  }

  toggleLowBeamLight() {
    var url = this.createUrl("cmd/l");
    return this.http.get(url).map(res => res.json());
  }

  toggleHeadLight() {
    var url = this.createUrl("cmd/h");
    return this.http.get(url).map(res => res.json());
  }

  doFlash() {
    var url = this.createUrl("cmd/f");
    return this.http.get(url).map(res => res.json());
  }

  toggleTurnLightLeft() {
    var url = this.createUrl("cmd/o");
    return this.http.get(url).map(res => res.json());
  }

  toggleTurnLightRight() {
    var url = this.createUrl("cmd/p");
    return this.http.get(url).map(res => res.json());
  }

  toggleWarningLights() {
    var url = this.createUrl("cmd/w");
    return this.http.get(url).map(res => res.json());
  }

  status() {
    var url = this.createUrl("status");
    return this.http.get(url).map(res => res.json());
  }
}

