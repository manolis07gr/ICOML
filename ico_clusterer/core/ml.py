import datetime
import pickle
import math

from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestRegressor

from core.utilities import ico_clusterer_features, ico_industries, ico_ann_remove_features, path_to_models, \
    etl_regression_target, etl_regression_features, etl_data_file


def udf_regress(row, model, feature):
  if math.isnan(row[feature]):
      return model.predict(row[etl_regression_target])[0]
  return row[feature]


def prepare_ico_data(raw_ico_data, save=False):
    industry_quantizer = lambda x: ico_industries.index(x)
    raw_ico_data.loc[:, 'industry'] = raw_ico_data['industry'].apply(industry_quantizer)

    rf = RandomForestRegressor(max_depth=2, random_state=0)

    median_raised = raw_ico_data[etl_regression_target].dropna().median()
    raw_ico_data.loc[:, etl_regression_target] = raw_ico_data.apply((lambda x: median_raised if math.isnan(x[etl_regression_target]) else x[etl_regression_target]), axis=1)

    for feature in etl_regression_features:
        temp_df = raw_ico_data[[feature, etl_regression_target]].dropna()
        y = temp_df[feature].as_matrix()
        X = temp_df[etl_regression_target].as_matrix().reshape(-1, 1)

        rf.fit(X, y)

        raw_ico_data.loc[:, feature] = raw_ico_data.apply(udf_regress, model=rf, feature = feature, axis=1)

    if save:
        raw_ico_data.to_csv(etl_data_file)
    return raw_ico_data


def generate_ico_models(etl_raw_ico_data, clusters_no=7, save=False):
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