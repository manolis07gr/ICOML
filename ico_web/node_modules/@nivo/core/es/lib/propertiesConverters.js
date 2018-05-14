/*
 * This file is part of the nivo project.
 *
 * Copyright 2016-present, Raphaël Benitte.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */
import _ from 'lodash-es';
import { format } from 'd3-format';

export var getLabelGenerator = function getLabelGenerator(_label, labelFormat) {
    var getRawLabel = _.isFunction(_label) ? _label : function (d) {
        return _.get(d, _label);
    };
    var formatter = void 0;
    if (labelFormat) {
        formatter = _.isFunction(labelFormat) ? labelFormat : format(labelFormat);
    }

    if (formatter) return function (d) {
        return formatter(getRawLabel(d));
    };
    return getRawLabel;
};

export var getAccessorFor = function getAccessorFor(directive) {
    return _.isFunction(directive) ? directive : function (d) {
        return d[directive];
    };
};