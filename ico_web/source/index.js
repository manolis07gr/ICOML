import ReactDOM from 'react-dom';
import React, {Component} from 'react';

import Radar from '../source/components/Radar'
import Clusterer from '../source/components/Clusterer'
import ClusterGrid from '../source/components/ClusterGrid'
import PrxChart from '../source/components/Chart'

import {cluster_data} from './dataset/data'
import {radar_ecosystem_data} from './dataset/data'
import {radar_cluster_1_data} from './dataset/data'
import {radar_cluster_2_data} from './dataset/data'
import {radar_cluster_3_data} from './dataset/data'
import {radar_cluster_4_data} from './dataset/data'
import {radar_cluster_5_data} from './dataset/data'
import {radar_cluster_6_data} from './dataset/data'
import {radar_cluster_7_data} from './dataset/data'

class App extends Component {
    constructor(props) {
        super(props);

        this.state = {cluster_chart_data:cluster_data,
                      radar_chart_data:radar_ecosystem_data,
                      selected_cluster:-1};

        this.cluster_callback_function = this.cluster_callback_function.bind(this);
    }

    cluster_callback_function(data) {
      //console.log("My Function Called with data:", data);
      var cluster_num = parseInt(data.substring(7).split(' ').join(''));

      this.setState({selected_cluster : cluster_num})

      switch (cluster_num) {
        case 1:
            this.setState({radar_chart_data : radar_cluster_1_data})
            break;
        case 2:
            this.setState({radar_chart_data : radar_cluster_2_data})
            break;
        case 3:
            this.setState({radar_chart_data : radar_cluster_3_data})
            break;
        case 4:
            this.setState({radar_chart_data : radar_cluster_4_data})
            break;
        case 5:
            this.setState({radar_chart_data : radar_cluster_5_data})
            break;
        case 6:
            this.setState({radar_chart_data : radar_cluster_6_data})
            break;
        case 7:
            this.setState({radar_chart_data : radar_cluster_7_data})
            break;
        default:
            this.setState({radar_chart_data : radar_ecosystem_data})
            break;
      }
    }

    render() {
    //console.log("APP RENDERING")
    //console.log("Current state :", this.state)
        return (
        <React.Fragment>
        <div class="row justify-content-md-center" >
            <div class="col" style={{ height: 450 }}><Clusterer chart_data={this.state.cluster_chart_data} cluster_callback_function = {this.cluster_callback_function}/></div>
            <div class="col" style={{ height: 450 }}><Radar chart_data={this.state.radar_chart_data} /></div>
            <div class="col" style={{ height: 450 }}><PrxChart/></div>
        </div>
        <div class="row justify-content-md-center" >
            <div class="col"><ClusterGrid/></div>
        </div>
        </React.Fragment>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('ico_dapp'));

