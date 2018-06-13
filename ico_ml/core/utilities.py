import pandas as pd
import glob
import os

from core.constants import  path_to_models, path_to_output


def construct_cluster_data(raw_ico_data, ico_data_model, clusters):
    consolidated_cluster_data = pd.DataFrame()
    raw_ico_data['cluster']= ico_data_model['cluster']
    for c in clusters:
        cluster_data = raw_ico_data[raw_ico_data['cluster'] == c]
        consolidated_cluster_data = consolidated_cluster_data.append(cluster_data)
    return consolidated_cluster_data


def reset_system():
    os.chdir(path_to_models)
    files = glob.glob('*.*')
    for filename in files:
        os.unlink(filename)

    os.chdir(path_to_output)
    files = glob.glob('*.*')
    for filename in files:
        os.unlink(filename)


