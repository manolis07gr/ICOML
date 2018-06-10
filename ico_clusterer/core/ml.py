import datetime
import pickle

from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from core.utilities import ico_clusterer_features, ico_industries, ico_ann_remove_features, path_to_models


def generate_ico_models(raw_ico_data, clusters_no=7, save=False):
    etl_raw_ico_data = raw_ico_data.dropna()

    ico_cluster_data_model = etl_raw_ico_data[ico_clusterer_features]
    industrizer = lambda x: ico_industries.index(x)
    ico_cluster_data_model.loc[:, 'industry'] = ico_cluster_data_model['industry'].apply(industrizer)

    k_means_model = KMeans(n_clusters=clusters_no, random_state=0).fit(ico_cluster_data_model)
    ico_ann_data_model = ico_cluster_data_model.drop(ico_ann_remove_features,1)

    X = ico_ann_data_model.as_matrix()
    y = k_means_model.labels_

    # TODO: Add grid optimisations
    ico_ann = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    ico_ann.fit(X, y)

    if save:
        now = datetime.datetime.now()
        timestamp = str(now.year)+str(now.month).zfill(2)+str(now.day).zfill(2)

        kmeans_model_filename = 'clusterer_'+ timestamp +'.pickle'
        full_path = path_to_models + kmeans_model_filename
        with open(full_path, 'wb') as f:
            pickle.dump(k_means_model, f)

        ann_model_filename = 'classifier_' + timestamp + '.pickle'
        full_path = path_to_models + ann_model_filename
        with open(full_path, 'wb') as f:
            pickle.dump(ico_ann, f)

        data_model_file = path_to_models + 'clusterer_data_'+ timestamp +'.csv'
        ico_cluster_data_model.to_csv(data_model_file, index=False)
    return k_means_model, ico_cluster_data_model, etl_raw_ico_data