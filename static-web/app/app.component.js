"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
var core_1 = require('@angular/core');
var bug_1 = require("./bug");
var platform_browser_1 = require('@angular/platform-browser');
var AppComponent = (function () {
    function AppComponent(bug, document) {
        this.bug = bug;
        this.document = document;
        this.status = {};
        //this.updateStatus()
        this.startLive();
        //console.log(this.document.location);
        this.bug.setBaseUrl(this.document.location.protocol + "//" + this.document.location.host + "/");
    }
    AppComponent.prototype.startLive = function () {
        var _this = this;
        this.statusThread = setInterval(function () { return _this.updateStatus(); }, 1500);
    };
    AppComponent.prototype.stopLive = function () {
        clearTimeout(this.statusThread);
    };
    AppComponent.prototype.toggleLowBeamLight = function () {
        var _this = this;
        this.bug.toggleLowBeamLight().subscribe(function () { _this.updateStatus(); }, function (err) { console.log(err); }, function () { });
    };
    AppComponent.prototype.toggleHeadLight = function () {
        var _this = this;
        this.bug.toggleHeadLight().subscribe(function () { _this.updateStatus(); }, function (err) { console.log(err); }, function () { });
    };
    AppComponent.prototype.doFlash = function () {
        var _this = this;
        this.bug.doFlash().subscribe(function () { _this.updateStatus(); }, function (err) { console.log(err); }, function () { });
    };
    AppComponent.prototype.toggleTurnLightLeft = function () {
        var _this = this;
        this.bug.toggleTurnLightLeft().subscribe(function () { _this.updateStatus(); }, function (err) { console.log(err); }, function () { });
    };
    AppComponent.prototype.toggleTurnLightRight = function () {
        var _this = this;
        this.bug.toggleTurnLightRight().subscribe(function () { _this.updateStatus(); }, function (err) { console.log(err); }, function () { });
    };
    AppComponent.prototype.toggleWarningLights = function () {
        var _this = this;
        this.bug.toggleWarningLights().subscribe(function () { _this.updateStatus(); }, function (err) { console.log(err); }, function () { });
    };
    AppComponent.prototype.updateStatus = function () {
        var _this = this;
        this.bug.status().subscribe(function (data) { _this.status = data; });
    };
    AppComponent = __decorate([
        core_1.Component({
            selector: 'bug',
            templateUrl: 'templates/bug.html',
            providers: [bug_1.BugService],
        }),
        __param(1, core_1.Inject(platform_browser_1.DOCUMENT)), 
        __metadata('design:paramtypes', [bug_1.BugService, Object])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map