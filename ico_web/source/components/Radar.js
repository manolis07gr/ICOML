import { render } from 'react-dom'
import React, {Component} from 'react';
import { ResponsiveRadar } from '@nivo/radar'

export default class Radar extends Component {
  constructor(props) {
    super(props);
    // console.log("RADAR CHART DATA:",props.chart_data);
    this.state = {chart_data:props.chart_data};
  }

  componentWillReceiveProps(nextProps) {
      this.setState({chart_data:nextProps.chart_data});
  }

  render(){
    // console.log("RADAR RENDERING")
    // console.log("PROPS RADAR CHART DATA:",this.props.chart_data);
    // console.log("STAETE RADAR CHART DATA:",this.state.chart_data);
    return(<ResponsiveRadar
        data = {this.state.chart_data}

        keys={[
            "Strongest",
            "Weakest",
            "Average"
        ]}

        indexBy="feature"

        margin={{
            "top": 70,
            "right": 80,
            "bottom": 40,
            "left": 80
        }}

        curve="catmullRomClosed"
        borderWidth={1}
        borderColor="inherit"
        gridLevels={8}
        gridShape="circular"
        gridLabelOffset={36}
        enableDots={true}
        dotSize={8}
        dotColor="inherit"
        dotBorderWidth={0}
        dotBorderColor="#ffffff"
        enableDotLabel={true}
        dotLabel="value"
        dotLabelYOffset={-12}
        colors="nivo"
        colorBy="key"
        fillOpacity={0.1}
        animate={true}
        motionStiffness={90}
        motionDamping={15}
        isInteractive={true}
        legends={[
            {
                "anchor": "top-left",
                "direction": "column",
                "translateX": -50,
                "translateY": -40,
                "itemWidth": 80,
                "itemHeight": 20,
                "symbolSize": 12,
                "symbolShape": "circle"
            }
        ]}
    />)
  }
}

