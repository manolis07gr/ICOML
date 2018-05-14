'use strict';

exports.__esModule = true;
exports.getColorsGenerator = exports.getColorRange = exports.nivoCategoricalColors = undefined;

var _inherit = require('./inherit');

Object.keys(_inherit).forEach(function (key) {
    if (key === "default" || key === "__esModule") return;
    Object.defineProperty(exports, key, {
        enumerable: true,
        get: function get() {
            return _inherit[key];
        }
    });
});

var _motion = require('./motion');

Object.keys(_motion).forEach(function (key) {
    if (key === "default" || key === "__esModule") return;
    Object.defineProperty(exports, key, {
        enumerable: true,
        get: function get() {
            return _motion[key];
        }
    });
});

var _quantize = require('./quantize');

Object.keys(_quantize).forEach(function (key) {
    if (key === "default" || key === "__esModule") return;
    Object.defineProperty(exports, key, {
        enumerable: true,
        get: function get() {
            return _quantize[key];
        }
    });
});

var _lodash = require('lodash');

var _lodash2 = _interopRequireDefault(_lodash);

var _d3Scale = require('d3-scale');

var _d3ScaleChromatic = require('d3-scale-chromatic');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var ordinalColorScales = {
    d310: (0, _d3Scale.scaleOrdinal)(_d3Scale.schemeCategory10),
    d320: (0, _d3Scale.scaleOrdinal)(_d3Scale.schemeCategory20),
    d320b: (0, _d3Scale.scaleOrdinal)(_d3Scale.schemeCategory20b),
    d320c: (0, _d3Scale.scaleOrdinal)(_d3Scale.schemeCategory20c),
    accent: (0, _d3Scale.scaleOrdinal)(_d3ScaleChromatic.schemeAccent),
    dark2: (0, _d3Scale.scaleOrdinal)(_d3ScaleChromatic.schemeDark2),
    paired: (0, _d3Scale.scaleOrdinal)(_d3ScaleChromatic.schemePaired),
    pastel1: (0, _d3Scale.scaleOrdinal)(_d3ScaleChromatic.schemePastel1),
    pastel2: (0, _d3Scale.scaleOrdinal)(_d3ScaleChromatic.schemePastel2),
    set1: (0, _d3Scale.scaleOrdinal)(_d3ScaleChromatic.schemeSet1),
    set2: (0, _d3Scale.scaleOrdinal)(_d3ScaleChromatic.schemeSet2),
    set3: (0, _d3Scale.scaleOrdinal)(_d3ScaleChromatic.schemeSet3)
}; /*
    * This file is part of the nivo project.
    *
    * Copyright 2016-present, Raphaël Benitte.
    *
    * For the full copyright and license information, please view the LICENSE
    * file that was distributed with this source code.
    */
var nivoCategoricalColors = exports.nivoCategoricalColors = function nivoCategoricalColors() {
    return (0, _d3Scale.scaleOrdinal)(['#e8c1a0', '#f47560', '#f1e15b', '#e8a838', '#61cdbb', '#97e3d5']);
};

var dataColor = function dataColor(d) {
    return d.color || d.data.color;
};

var getColorRange = exports.getColorRange = function getColorRange(instruction) {
    if (instruction === 'data') return dataColor;

    if (instruction === 'nivo') return nivoCategoricalColors();

    if (_lodash2.default.isFunction(instruction)) return instruction;

    if (ordinalColorScales[instruction]) return ordinalColorScales[instruction];

    if (_lodash2.default.isArray(instruction)) return (0, _d3Scale.scaleOrdinal)(instruction);

    return function () {
        return instruction;
    };
};

var getColorsGenerator = exports.getColorsGenerator = function getColorsGenerator(colors, colorBy) {
    // skip range, color should be bound to data
    if (_lodash2.default.isFunction(colorBy)) return colorBy;

    var scale = void 0;
    var getColorId = function getColorId(d) {
        return _lodash2.default.get(d, colorBy);
    };

    if (colors === 'nivo') {
        // use default nivo categorical colors
        scale = nivoCategoricalColors();
    } else if (ordinalColorScales[colors]) {
        // use predefined d3 ordinal color scale
        scale = ordinalColorScales[colors];
    } else if (_lodash2.default.isArray(colors)) {
        // user defined color range
        scale = (0, _d3Scale.scaleOrdinal)(colors);
    } else {
        // just use provided value, all elements will have identical color
        return function (d) {
            return colors;
        };
    }

    return function (d) {
        return scale(getColorId(d));
    };
};