import datetime
import pickle
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier

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


def ico_clusterer(raw_ico_data, clusters_no=7, save=False):
    raw_ico_data = raw_ico_data.dropna()

    ico_data_model = raw_ico_data[ico_clusterer_features]
    industrizer = lambda x: ico_industries.index(x)
    ico_data_model['industry'] = ico_data_model['industry'].apply(industrizer)

    k_means_model = KMeans(n_clusters=clusters_no, random_state=0).fit(ico_data_model)
    ico_data_model = ico_data_model.drop(ico_ann_remove_features,1)

    X = ico_data_model.as_matrix()
    y = k_means_model.labels_

    ico_ann = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    ico_ann.fit(X, y)

    if save:
        now = datetime.datetime.now()
        timestamp = str(now.year)+str(now.month).zfill(2)+str(now.day).zfill(2)

        path_to_file = './models/'

        kmeans_model_filename = 'clusterer_'+ timestamp +'.pickle'
        full_path = path_to_file + kmeans_model_filename
        with open(full_path, 'wb') as f:
            pickle.dump(k_means_model, f)

        ann_model_filename = 'classifier_' + timestamp + '.pickle'
        full_path = path_to_file + ann_model_filename
        with open(full_path, 'wb') as f:
            pickle.dump(ico_ann, f)

        data_model_file = path_to_file + 'clusterer_data_'+ timestamp +'.csv'
        ico_data_model.to_csv(data_model_file, index=False)
    return k_means_model, ico_data_model