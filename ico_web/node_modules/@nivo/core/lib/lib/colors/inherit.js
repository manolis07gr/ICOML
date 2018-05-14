'use strict';

exports.__esModule = true;
exports.getInheritedColorGenerator = undefined;

var _lodash = require('lodash');

var _d3Color = require('d3-color');

/**
 * Memoize both color generator & color generator result.
 */
/*
 * This file is part of the nivo project.
 *
 * Copyright 2016-present, Raphaël Benitte.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */
var memoizedColorModifier = (0, _lodash.memoize)(function (method, _amount) {
    var amount = parseFloat(_amount);

    return (0, _lodash.memoize)(function (d) {
        return (0, _d3Color.rgb)(d.color)[method](amount).toString();
    }, function (d) {
        return d.color;
    });
}, function (method, amount) {
    return method + '.' + amount;
});

var noneGenerator = function noneGenerator() {
    return 'none';
};
var inheritGenerator = function inheritGenerator(d) {
    return d.color;
};

/**
 * @param {string|Function} instruction
 * @param {string}          [themeKey]
 * @return {Function}
 */
var getInheritedColorGenerator = exports.getInheritedColorGenerator = function getInheritedColorGenerator(instruction, themeKey) {
    if (instruction === 'none') return noneGenerator;

    if ((0, _lodash.isFunction)(instruction)) return instruction;

    if (instruction === 'theme') {
        if (!themeKey) {
            throw new Error('Cannot use \'theme\' directive without providing \'themeKey\'');
        }

        return function (d, theme) {
            return (0, _lodash.get)(theme, themeKey);
        };
    }

    if (instruction === 'inherit') return inheritGenerator;

    var inheritMatches = instruction.match(/inherit:(darker|brighter)\(([0-9.]+)\)/);
    if (inheritMatches) {
        var method = inheritMatches[1];
        var amount = inheritMatches[2];

        return memoizedColorModifier(method, amount);
    }

    return function () {
        return instruction;
    };
};