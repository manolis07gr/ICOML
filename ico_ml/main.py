import pandas as pd

from core.ml import generate_ico_models, prepare_ico_data
from core.utilities import reset_system
from core.constants import raw_data_file
from ui.json import generate_frontend_data

reset_system()

raw_ico_data = pd.read_csv(raw_data_file)

etl_raw_ico_data = prepare_ico_data(raw_ico_data, save=True)

cluster_model, ico_cluster_data_model, etl_raw_ico_data = generate_ico_models(etl_raw_ico_data, save=True)
ico_cluster_data_model['cluster'] = cluster_model.labels_

labels = set(cluster_model.labels_)
if generate_frontend_data(etl_raw_ico_data, ico_cluster_data_model, labels):
    print("Front-end data generated succesfully!")



