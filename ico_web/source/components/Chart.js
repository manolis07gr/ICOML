import { render } from 'react-dom'
import { ResponsiveLine } from '@nivo/line'

import React, {Component} from 'react';

export default class PrxChart extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return(
            <ResponsiveLine
            data={[
  {
    "id": "whisky",
    "color": "hsl(89, 70%, 50%)",
    "data": [
      {
        "color": "hsl(220, 70%, 50%)",
        "x": "MO",
        "y": 33
      },
      {
        "color": "hsl(213, 70%, 50%)",
        "x": "TR",
        "y": 0
      },
      {
        "color": "hsl(322, 70%, 50%)",
        "x": "TG",
        "y": 32
      },
      {
        "color": "hsl(286, 70%, 50%)",
        "x": "IN",
        "y": 59
      },
      {
        "color": "hsl(28, 70%, 50%)",
        "x": "SR",
        "y": 2
      },
      {
        "color": "hsl(275, 70%, 50%)",
        "x": "BL",
        "y": 58
      },
      {
        "color": "hsl(339, 70%, 50%)",
        "x": "NG",
        "y": 7
      },
      {
        "color": "hsl(51, 70%, 50%)",
        "x": "BN",
        "y": 39
      },
      {
        "color": "hsl(285, 70%, 50%)",
        "x": "KZ",
        "y": 1
      }
    ]
  },
  {
    "id": "rhum",
    "color": "hsl(257, 70%, 50%)",
    "data": [
      {
        "color": "hsl(65, 70%, 50%)",
        "x": "MO",
        "y": 41
      },
      {
        "color": "hsl(311, 70%, 50%)",
        "x": "TR",
        "y": 31
      },
      {
        "color": "hsl(209, 70%, 50%)",
        "x": "TG",
        "y": 1
      },
      {
        "color": "hsl(126, 70%, 50%)",
        "x": "IN",
        "y": 9
      },
      {
        "color": "hsl(170, 70%, 50%)",
        "x": "SR",
        "y": 41
      },
      {
        "color": "hsl(192, 70%, 50%)",
        "x": "BL",
        "y": 41
      },
      {
        "color": "hsl(157, 70%, 50%)",
        "x": "NG",
        "y": 38
      },
      {
        "color": "hsl(33, 70%, 50%)",
        "x": "BN",
        "y": 31
      },
      {
        "color": "hsl(11, 70%, 50%)",
        "x": "KZ",
        "y": 31
      }
    ]
  },
  {
    "id": "gin",
    "color": "hsl(76, 70%, 50%)",
    "data": [
      {
        "color": "hsl(266, 70%, 50%)",
        "x": "MO",
        "y": 10
      },
      {
        "color": "hsl(171, 70%, 50%)",
        "x": "TR",
        "y": 19
      },
      {
        "color": "hsl(11, 70%, 50%)",
        "x": "TG",
        "y": 56
      },
      {
        "color": "hsl(173, 70%, 50%)",
        "x": "IN",
        "y": 14
      },
      {
        "color": "hsl(157, 70%, 50%)",
        "x": "SR",
        "y": 20
      },
      {
        "color": "hsl(55, 70%, 50%)",
        "x": "BL",
        "y": 39
      },
      {
        "color": "hsl(359, 70%, 50%)",
        "x": "NG",
        "y": 43
      },
      {
        "color": "hsl(249, 70%, 50%)",
        "x": "BN",
        "y": 0
      },
      {
        "color": "hsl(78, 70%, 50%)",
        "x": "KZ",
        "y": 47
      }
    ]
  },
  {
    "id": "vodka",
    "color": "hsl(243, 70%, 50%)",
    "data": [
      {
        "color": "hsl(326, 70%, 50%)",
        "x": "MO",
        "y": 32
      },
      {
        "color": "hsl(40, 70%, 50%)",
        "x": "TR",
        "y": 34
      },
      {
        "color": "hsl(231, 70%, 50%)",
        "x": "TG",
        "y": 17
      },
      {
        "color": "hsl(192, 70%, 50%)",
        "x": "IN",
        "y": 31
      },
      {
        "color": "hsl(30, 70%, 50%)",
        "x": "SR",
        "y": 30
      },
      {
        "color": "hsl(322, 70%, 50%)",
        "x": "BL",
        "y": 33
      },
      {
        "color": "hsl(224, 70%, 50%)",
        "x": "NG",
        "y": 55
      },
      {
        "color": "hsl(132, 70%, 50%)",
        "x": "BN",
        "y": 23
      },
      {
        "color": "hsl(157, 70%, 50%)",
        "x": "KZ",
        "y": 11
      }
    ]
  },
  {
    "id": "cognac",
    "color": "hsl(120, 70%, 50%)",
    "data": [
      {
        "color": "hsl(311, 70%, 50%)",
        "x": "MO",
        "y": 60
      },
      {
        "color": "hsl(351, 70%, 50%)",
        "x": "TR",
        "y": 12
      },
      {
        "color": "hsl(52, 70%, 50%)",
        "x": "TG",
        "y": 41
      },
      {
        "color": "hsl(237, 70%, 50%)",
        "x": "IN",
        "y": 3
      },
      {
        "color": "hsl(18, 70%, 50%)",
        "x": "SR",
        "y": 3
      },
      {
        "color": "hsl(139, 70%, 50%)",
        "x": "BL",
        "y": 20
      },
      {
        "color": "hsl(87, 70%, 50%)",
        "x": "NG",
        "y": 23
      },
      {
        "color": "hsl(303, 70%, 50%)",
        "x": "BN",
        "y": 55
      },
      {
        "color": "hsl(8, 70%, 50%)",
        "x": "KZ",
        "y": 54
      }
    ]
  }
]}
            margin={{
                "top": 50,
                "right": 110,
                "bottom": 50,
                "left": 60
            }}
            minY="auto"
            stacked={true}
            axisBottom={{
                "orient": "bottom",
                "tickSize": 5,
                "tickPadding": 5,
                "tickRotation": 0,
                "legend": "country code",
                "legendOffset": 36,
                "legendPosition": "center"
            }}
            axisLeft={{
                "orient": "left",
                "tickSize": 5,
                "tickPadding": 5,
                "tickRotation": 0,
                "legend": "count",
                "legendOffset": -40,
                "legendPosition": "center"
            }}
            dotSize={10}
            dotColor="inherit:darker(0.3)"
            dotBorderWidth={2}
            dotBorderColor="#ffffff"
            enableDotLabel={true}
            dotLabel="y"
            dotLabelYOffset={-12}
            animate={true}
            motionStiffness={90}
            motionDamping={15}
            legends={[
                {
                    "anchor": "bottom-right",
                    "direction": "column",
                    "translateX": 100,
                    "itemWidth": 80,
                    "itemHeight": 20,
                    "symbolSize": 12,
                    "symbolShape": "circle"
                }
            ]}
        />)
    }
}