'use strict';

exports.__esModule = true;

var _markers = require('./markers');

Object.keys(_markers).forEach(function (key) {
  if (key === "default" || key === "__esModule") return;
  Object.defineProperty(exports, key, {
    enumerable: true,
    get: function get() {
      return _markers[key];
    }
  });
});