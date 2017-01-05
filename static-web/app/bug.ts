/**
 * Created by tspycher on 04.01.17.
 */
import 'rxjs/add/operator/map'
import {Http} from "@angular/http";

export class BugService {
  static get parameters() {
    return [[Http]];
  }

  constructor (private http:Http) {

  }

  toggleLowBeamLight() {
    var url = "/cmd/l";
    return this.http.get(url).map(res => res.json());
  }

  toggleHeadLight() {
    var url = "/cmd/h";
    return this.http.get(url).map(res => res.json());
  }

  doFlash() {
    var url = "/cmd/f";
    return this.http.get(url).map(res => res.json());
  }

  toggleTurnLightLeft() {
    var url = "/cmd/o";
    return this.http.get(url).map(res => res.json());
  }

  toggleTurnLightRight() {
    var url = "/cmd/p";
    return this.http.get(url).map(res => res.json());
  }

  toggleWarningLights() {
    var url = "/cmd/w";
    return this.http.get(url).map(res => res.json());
  }

  status() {
    var url = "/status";
    return this.http.get(url).map(res => res.json());
  }
}
