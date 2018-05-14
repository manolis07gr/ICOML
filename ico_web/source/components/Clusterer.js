import { render } from 'react-dom'
import React, {Component} from 'react';
import { ResponsiveBubble } from '@nivo/circle-packing'

import {cluster_data} from '../dataset/data'

export default class Clusterer extends Component {
    constructor(props) {
        super(props);
        this.state = {chart_data:props.chart_data};
    }

    handleNodeClick = (node, event) => {
            // alert(`${node.id}: ${node.value}\nclicked at x: ${event.clientX}, y: ${event.clientY}`)
            this.props.cluster_callback_function(node.id);
    }

    render(){
        // console.log("CLUSTERER RENDERING")
        return(<ResponsiveBubble
            root={this.state.chart_data}

            margin={{
                "top": 20,
                "right": 20,
                "bottom": 20,
                "left": 20
            }}

            identity="name"
            value="loc"
            colors="d320c"
            colorBy="depth"
            padding={6}
            labelTextColor="inherit:darker(0.8)"
            borderWidth={1}
            borderColor="inherit:darker(1.2)"
            onClick={this.handleNodeClick}

            defs={[
                {
                    "id": "lines",
                    "type": "patternLines",
                    "background": "none",
                    "color": "inherit",
                    "rotation": -45,
                    "lineWidth": 5,
                    "spacing": 8
                }
            ]}

            fill={[
                {
                    "match": {
                        "depth": 1
                    },
                    "id": "lines"
                }
            ]}

            animate={true}
            motionStiffness={90}
            motionDamping={12}
        />)
    }
}