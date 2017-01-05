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
    var url = "http://10.84.1.108/cmd/l";
    return this.http.get(url).map(res => res.json());
  }

  toggleHeadLight() {
    var url = "http://10.84.1.108/cmd/h";
    return this.http.get(url).map(res => res.json());
  }

  doFlash() {
    var url = "http://10.84.1.108/cmd/f";
    return this.http.get(url).map(res => res.json());
  }

  toggleTurnLightLeft() {
    var url = "http://10.84.1.108/cmd/o";
    return this.http.get(url).map(res => res.json());
  }

  toggleTurnLightRight() {
    var url = "http://10.84.1.108/cmd/p";
    return this.http.get(url).map(res => res.json());
  }

  toggleWarningLights() {
    var url = "http://10.84.1.108/cmd/w";
    return this.http.get(url).map(res => res.json());
  }

  status() {
    var url = "http://10.84.1.108/status";
    return this.http.get(url).map(res => res.json());
  }
}
