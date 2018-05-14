'use strict';

exports.__esModule = true;
exports.getAccessorFor = exports.getLabelGenerator = undefined;

var _lodash = require('lodash');

var _lodash2 = _interopRequireDefault(_lodash);

var _d3Format = require('d3-format');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

/*
 * This file is part of the nivo project.
 *
 * Copyright 2016-present, Raphaël Benitte.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */
var getLabelGenerator = exports.getLabelGenerator = function getLabelGenerator(_label, labelFormat) {
    var getRawLabel = _lodash2.default.isFunction(_label) ? _label : function (d) {
        return _lodash2.default.get(d, _label);
    };
    var formatter = void 0;
    if (labelFormat) {
        formatter = _lodash2.default.isFunction(labelFormat) ? labelFormat : (0, _d3Format.format)(labelFormat);
    }

    if (formatter) return function (d) {
        return formatter(getRawLabel(d));
    };
    return getRawLabel;
};

var getAccessorFor = exports.getAccessorFor = function getAccessorFor(directive) {
    return _lodash2.default.isFunction(directive) ? directive : function (d) {
        return d[directive];
    };
};