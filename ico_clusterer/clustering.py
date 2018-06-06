import pandas as pd
import matplotlib.pyplot as plt
import shutil

from sklearn.cluster import KMeans
from core.utilities import export_cluster_radar_json, construct_cluster_data, export_cluster_regression

raw_ico_data = pd.read_csv('../data/ico_data_raw.csv')

ico_model_features = ['age', 'region', 'industry',
                      'hardcap', 'raised',
                      'telegram', 'team', 'N_google_news', 'N_twitter',
                      'price', 'ret_ico_to_day_one']

radar_chart_features = ['age', 'hardcap', 'raised',
                        'telegram', 'team', 'N_google_news', 'N_twitter',
                        'price', 'ret_ico_to_day_one']

raw_ico_data = raw_ico_data.dropna()

ico_data_model = raw_ico_data[ico_model_features]
ico_data_model = pd.get_dummies(data=ico_data_model, columns=['region', 'industry'])

clustering_clusters = 7

k_means_model = KMeans(n_clusters=clustering_clusters, random_state=0).fit(ico_data_model)

log_returns = ico_data_model['ret_ico_to_day_one'].as_matrix()

#plt.scatter(k_means_model.labels_, log_returns, c=k_means_model.labels_)
#plt.title("Cluster of log returns")
#plt.show()

raw_ico_data['cluster'] = k_means_model.labels_


ico_ecosystem_file = open("./output/ico_clusters.json", "w+")

print("""{\"name\": \"ICO Ecosystem\",\"children\": [""", file=ico_ecosystem_file)
money_raised_max = 0
money_raised_min = 10000000000

avg_cluster_data = {}
for radar_chart_feature in radar_chart_features:
    avg_cluster_data[radar_chart_feature] = 0

no_icos = 0
labels = set(k_means_model.labels_)
no_clusters = len(labels)
consolidated_cluster_data = construct_cluster_data(raw_ico_data, labels)


for c in labels:
    print("""{\"name\": \"Cluster """, c + 1, """\",\"children\": [""", file=ico_ecosystem_file)
    ix = 0
    cluster_data = consolidated_cluster_data[consolidated_cluster_data['cluster'] == c]
    for row in cluster_data.iterrows():
        no_icos += 1
        current_money_raised = row[1]['raised']
        if current_money_raised > money_raised_max:
            strongest_ico = row[1]['coin']
            money_raised_max = current_money_raised
        if current_money_raised < money_raised_min:
            weakest_ico = row[1]['coin']
            money_raised_min = current_money_raised

        for radar_chart_feature in radar_chart_features:
            avg_cluster_data[radar_chart_feature] += int(row[1][radar_chart_feature])

        print("""{\"name\": \"""", row[1]['coin'], """\",\"loc\":""", row[1]['raised'], end='', file=ico_ecosystem_file)

        if ix + 1 < len(cluster_data.index):
            print("},",  file=ico_ecosystem_file)
        else:
            print("}", file=ico_ecosystem_file)
        ix += 1

    if c < no_clusters-1:
        print("]},", file=ico_ecosystem_file)
    else:
        print("]}", file=ico_ecosystem_file)
print("""]}""", file=ico_ecosystem_file)

strongest_ico_data = raw_ico_data[raw_ico_data['coin'] == strongest_ico]
weakest_ico_data = raw_ico_data[raw_ico_data['coin'] == weakest_ico]

for radar_chart_feature in radar_chart_features:
    avg_cluster_data[radar_chart_feature] /= no_icos
    avg_cluster_data[radar_chart_feature] = round(avg_cluster_data[radar_chart_feature], 2)


print("ICO CLUSTERS", labels)
print("-----------------------------")
print("Winning ICO:", strongest_ico_data)
print("Weakest ICO:", weakest_ico_data)

file_name = "radar_ecosystem_data.json"
export_cluster_radar_json(radar_chart_features, strongest_ico_data, weakest_ico_data, avg_cluster_data, file_name)

export_cluster_regression(consolidated_cluster_data, "ecosystem_regression.json")

for c in labels:
    cluster_data = consolidated_cluster_data[consolidated_cluster_data['cluster'] == c]
    for row in cluster_data.iterrows():
        no_icos += 1
        current_money_raised = row[1]['raised']
        if current_money_raised > money_raised_max:
            strongest_ico = row[1]['coin']
            money_raised_max = current_money_raised
        if current_money_raised < money_raised_min:
            weakest_ico = row[1]['coin']
            money_raised_min = current_money_raised

        for radar_chart_feature in radar_chart_features:
            avg_cluster_data[radar_chart_feature] += int(row[1][radar_chart_feature])

    strongest_ico_data = raw_ico_data[raw_ico_data['coin'] == strongest_ico]
    weakest_ico_data = raw_ico_data[raw_ico_data['coin'] == weakest_ico]

    for radar_chart_feature in radar_chart_features:
        avg_cluster_data[radar_chart_feature] /= no_icos
        avg_cluster_data[radar_chart_feature] = round(avg_cluster_data[radar_chart_feature], 2)

    print("ICO CLUSTER", str(c))
    print("-----------------------------")
    print("Winning ICO:", strongest_ico_data)
    print("Weakest ICO:", weakest_ico_data)

    file_name = "radar_cluster_"+str(c+1)+".json"
    export_cluster_radar_json(radar_chart_features, strongest_ico_data, weakest_ico_data, avg_cluster_data, file_name)
    regression_file_name = "cluster_" + str(c + 1) + "_regression.json"
    export_cluster_regression(consolidated_cluster_data, regression_file_name)