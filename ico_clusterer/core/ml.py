import pandas as pd
from sklearn.cluster import KMeans

ico_industries =['blockchain', 'entertainment', 'fintech',
                 'insurance services', 'saas', 'telecommunications',
                 'transportation', 'other','ecommerce', 'real estate']

ico_clusterer_features = ['age', 'region', 'industry',
                      'hardcap', 'raised',
                      'telegram', 'team', 'N_google_news', 'N_twitter',
                      'price', 'ret_ico_to_day_one']

ico_ann_remove_features = ['raised', 'ret_ico_to_day_one']

radar_chart_features = ['age', 'hardcap', 'raised',
                        'telegram', 'team', 'N_google_news', 'N_twitter',
                        'price', 'ret_ico_to_day_one']


def ico_clusterer(raw_ico_data):
    raw_ico_data = raw_ico_data.dropna()

    ico_data_model = raw_ico_data[ico_clusterer_features]
    industrizer = lambda x: ico_industries.index(x)
    ico_data_model['industry'] = ico_data_model['industry'].apply(industrizer)

    clustering_clusters = 7

    k_means_model = KMeans(n_clusters=clustering_clusters, random_state=0).fit(ico_data_model)
    return k_means_model, ico_data_model