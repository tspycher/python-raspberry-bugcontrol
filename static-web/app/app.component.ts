import { Component, Inject } from '@angular/core';
import {BugService} from "./bug";
import { DOCUMENT } from '@angular/platform-browser';


@Component({
  selector: 'bug',
  templateUrl: 'templates/bug.html',
  providers: [BugService],
})
export class AppComponent  {

      private statusThread:any;

      constructor(private bug:BugService, @Inject(DOCUMENT) private document:any) {
          //this.updateStatus()
          this.startLive();
          //console.log(this.document.location);
          this.bug.setBaseUrl(this.document.location.protocol+"//"+this.document.location.host+"/");
      }

      startLive() {
        this.statusThread = setInterval(() => this.updateStatus(), 1500);
      }

      stopLive() {
        clearTimeout(this.statusThread);
      }

      toggleLowBeamLight() {
        this.bug.toggleLowBeamLight().subscribe(() => { this.updateStatus(); }, err => {console.log(err);}, () => {} );
      }

      toggleHeadLight() {
        this.bug.toggleHeadLight().subscribe(() => { this.updateStatus(); }, err => {console.log(err);}, () => {} );
      }

      doFlash() {
        this.bug.doFlash().subscribe(() => { this.updateStatus(); }, err => {console.log(err);}, () => {} );
      }

      toggleTurnLightLeft() {
        this.bug.toggleTurnLightLeft().subscribe(() => { this.updateStatus(); }, err => {console.log(err);}, () => {} );
      }

      toggleTurnLightRight() {
        this.bug.toggleTurnLightRight().subscribe(() => { this.updateStatus(); }, err => {console.log(err);}, () => {} );
      }

      toggleWarningLights() {
        this.bug.toggleWarningLights().subscribe(() => { this.updateStatus(); }, err => {console.log(err);}, () => {} );
      }

      public status:Object = {};

      private updateStatus() {
        this.bug.status().subscribe(data => {this.status = data});
      }
}
