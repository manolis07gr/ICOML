import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from core.utilities import export_cluster_radar_json, construct_cluster_data

raw_ico_data = pd.read_csv('./data/ICO_data_refactored.csv')

ico_model_features = ['age_days', 'country', 'industry',
                      'hardcap', 'money_raised', 'pct_complete',
                      'hardcap_reached', 'token_prx', 'followers',
                      'team_size', 'cum_years_experience', 'accredited_advisors',
                      'media_mentions', 'listing_prx', 'log_rets']

radar_chart_features = ['money_raised',
                        'team_size',
                        'accredited_advisors',
                        'cum_years_experience',
                        'age_days']

raw_ico_data = raw_ico_data.dropna()

ico_data_model = raw_ico_data[ico_model_features]
ico_data_model = pd.get_dummies(data=ico_data_model, columns=['country', 'industry', 'hardcap_reached'])

clustering_clusters = 7

k_means_model = KMeans(n_clusters=clustering_clusters, random_state=0).fit(ico_data_model)

log_returns = ico_data_model['log_rets'].as_matrix()

#plt.scatter(k_means_model.labels_, log_returns, c=k_means_model.labels_)
#plt.title("Cluster of log returns")
#plt.show()

raw_ico_data['cluster'] = k_means_model.labels_

print("""{\"name\": \"ICO Ecosystem\",\"children\": [""")
money_raised_max = 0
money_raised_min = 10000000000

avg_cluster_data = {}
for radar_chart_feature in radar_chart_features:
    avg_cluster_data[radar_chart_feature] = 0

no_icos = 0
labels = set(k_means_model.labels_)
labels = set([6])
no_clusters = len(labels)
consolidated_cluster_data = construct_cluster_data(raw_ico_data, labels)

for c in labels:
    print("""{\"name\": \"Cluster """, c + 1, """\",\"children\": [""")
    ix = 0
    cluster_data = consolidated_cluster_data[consolidated_cluster_data['cluster'] == c]
    for row in cluster_data.iterrows():
        no_icos += 1
        current_money_raised = row[1]['money_raised']
        if current_money_raised > money_raised_max:
            strongest_ico = row[1]['ico_name']
            money_raised_max = current_money_raised
        if current_money_raised < money_raised_min:
            weakest_ico = row[1]['ico_name']
            money_raised_min = current_money_raised

        for radar_chart_feature in radar_chart_features:
            avg_cluster_data[radar_chart_feature] += int(row[1][radar_chart_feature])

        print("""{\"name\": \"""", row[1]['ico_name'], """\",\"loc\":""", row[1]['money_raised'], """}""", end='')
        if ix + 1 < len(cluster_data.index):
            print(",")
        ix += 1
    print("""]}""", end='')
    if c < no_clusters-1:
        print(",")
    print("""]}""")

strongest_ico_data = raw_ico_data[raw_ico_data['ico_name'] == strongest_ico]
weakest_ico_data = raw_ico_data[raw_ico_data['ico_name'] == weakest_ico]

for radar_chart_feature in radar_chart_features:
    avg_cluster_data[radar_chart_feature] /= no_icos
    avg_cluster_data[radar_chart_feature] = round(avg_cluster_data[radar_chart_feature], 2)


print("ICO CLUSTERS", labels)
print("-----------------------------")
print("Winning ICO:", strongest_ico_data)
print("Weakest ICO:", weakest_ico_data)

export_cluster_radar_json(radar_chart_features, strongest_ico_data, weakest_ico_data, avg_cluster_data)