import pandas as pd
import glob
import os

path_to_data = "C:/Users/tsapi/Documents/GitHub/icoml/ico_clusterer/data/"
path_to_models = "C:/Users/tsapi/Documents/GitHub/icoml/ico_clusterer/models/"
path_to_output = "C:/Users/tsapi/Documents/GitHub/icoml/ico_clusterer/output/"

raw_data_file_name = "ico_data_raw.csv"
ecosystems_clusters_file_name = "ico_clusters.json"
ecosystem_radar_file_name = "radar_ecosystem_data.json"
ecosystem_regression_file_name = "ecosystem_regression.out"
raw_data_file = path_to_data + raw_data_file_name
etl_data_file = path_to_data + "etl_ico_data_raw.csv"
ico_industries =['blockchain', 'entertainment', 'fintech',
                 'insurance services', 'saas', 'telecommunications',
                 'transportation', 'other','ecommerce', 'real estate',
                 'energy', 'social services']

ico_clusterer_features = ['age', 'region', 'industry',
                          'hardcap', 'raised',
                          'telegram', 'team', 'N_google_news',
                          'price', 'ret_ico_to_day_one']

ico_ann_remove_features = ['age', 'raised', 'ret_ico_to_day_one']


radar_chart_features = ['age', 'hardcap', 'raised',
                        'telegram', 'team', 'N_google_news', 'N_twitter',
                        'price', 'ret_ico_to_day_one']


etl_regression_features = ['hardcap', 'N_twitter', 'hype', 'telegram', 'team', 'N_google_news', 'price']
etl_regression_target = 'raised'

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


