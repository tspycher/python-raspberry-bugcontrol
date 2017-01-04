"use strict";
/**
 * Created by tspycher on 04.01.17.
 */
require('rxjs/add/operator/map');
var http_1 = require("@angular/http");
var BugService = (function () {
    function BugService(http) {
        this.http = http;
    }
    Object.defineProperty(BugService, "parameters", {
        get: function () {
            return [[http_1.Http]];
        },
        enumerable: true,
        configurable: true
    });
    BugService.prototype.toggleLowBeamLight = function () {
        var url = "http://127.0.0.1:5000/cmd/l";
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.toggleHeadLight = function () {
        var url = "http://127.0.0.1:5000/cmd/h";
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.doFlash = function () {
        var url = "http://127.0.0.1:5000/cmd/f";
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.toggleTurnLightLeft = function () {
        var url = "http://127.0.0.1:5000/cmd/o";
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.toggleTurnLightRight = function () {
        var url = "http://127.0.0.1:5000/cmd/p";
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.toggleWarningLights = function () {
        var url = "http://127.0.0.1:5000/cmd/w";
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    BugService.prototype.status = function () {
        var url = "http://127.0.0.1:5000/status";
        return this.http.get(url).map(function (res) { return res.json(); });
    };
    return BugService;
}());
exports.BugService = BugService;
//# sourceMappingURL=bug.js.map