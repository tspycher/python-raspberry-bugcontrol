"use strict";
/**
 * Created by tspycher on 04.01.17.
 */
require('rxjs/add/operator/map');
var http_1 = require("@angular/http");
var BugService = (function () {
    function BugService(http) {
        this.http = http;
        this.setBaseUrl("http://127.0.0.1:5000/");
    }
    Object.defineProperty(BugService, "parameters", {
        get: function () {
            return [[http_1.Http]];
        },
        enumerable: true,
        configurable: true
    });
    BugService.prototype.setBaseUrl = function (url) {
        this.baseurl = url;
    };
    BugService.prototype.createUrl = function (url) {
        return this.baseurl + url;
    };
    BugService.prototype.toggleLowBeamLight = function () {
        var url = this.createUrl("cmd/l");
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.toggleHeadLight = function () {
        var url = this.createUrl("cmd/h");
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.doFlash = function () {
        var url = this.createUrl("cmd/f");
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.toggleTurnLightLeft = function () {
        var url = this.createUrl("cmd/o");
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.toggleTurnLightRight = function () {
        var url = this.createUrl("cmd/p");
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.toggleWarningLights = function () {
        var url = this.createUrl("cmd/w");
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.status = function () {
        var url = this.createUrl("status");
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    return BugService;
}());
exports.BugService = BugService;
//# sourceMappingURL=bug.js.map