###############################
#      PATHS & FILENAMES      #
###############################
project_path = "C:/Users/tsapi/Documents/GitHub/icoml/ico_ml/"

path_to_data = project_path + "data/"
path_to_etl_data = project_path + "etl/"
path_to_models = project_path + "models/"
path_to_output = project_path + "output/"

raw_data_file_name = "ico_data_raw.csv"
ecosystems_clusters_file_name = "ico_clusters.json"
ecosystem_radar_file_name = "radar_ecosystem_data.json"
ecosystem_regression_file_name = "ecosystem_regression.out"
etl_data_file_name = "etl_ico_data_raw.csv"

raw_data_file = path_to_data + raw_data_file_name
etl_data_file = path_to_etl_data + etl_data_file_name


###############################
#        VARIOUS DICTS        #
###############################
ico_industries =['blockchain', 'entertainment', 'fintech',
                 'insurance services', 'saas', 'telecommunications',
                 'transportation', 'other','ecommerce', 'real estate',
                 'energy', 'social services']


###############################
#         ML CONSTANTS        #
###############################
ico_clusterer_features = ['age', 'region', 'industry',
                          'hardcap', 'raised',
                          'telegram', 'team', 'N_google_news',
                          'price', 'ret_ico_to_day_one']

ico_ann_remove_features = ['age', 'raised', 'ret_ico_to_day_one']


radar_chart_features = ['age', 'hardcap', 'raised',
                        'telegram', 'team', 'N_google_news', 'N_twitter',
                        'price', 'ret_ico_to_day_one']

cluster_regression_formula = "raised ~ team + hardcap + telegram + N_google_news + N_twitter"

###############################
#    ETL REGRESSION PROCESS   #
###############################
etl_regression_features = ['hardcap', 'N_twitter', 'hype', 'telegram', 'team', 'N_google_news', 'price']
etl_regression_target = 'raised'

