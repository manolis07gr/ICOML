import pandas as pd

from core.ml import generate_ico_models
from core.utilities import raw_data_file, reset_system
from ui.json import generate_frontend_data

reset_system()

raw_ico_data = pd.read_csv(raw_data_file)
cluster_model, ico_cluster_data_model, etl_raw_ico_data = generate_ico_models(raw_ico_data, save=True)
ico_cluster_data_model['cluster'] = cluster_model.labels_

labels = set(cluster_model.labels_)
if generate_frontend_data(etl_raw_ico_data, ico_cluster_data_model, labels):
    print("Front-end data generated succesfully!")



