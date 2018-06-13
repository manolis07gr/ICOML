from math import log10

from core.constants import radar_chart_features, ecosystem_radar_file_name, \
    ecosystem_regression_file_name, path_to_output, ecosystems_clusters_file_name, cluster_regression_formula
from core.ml import regress_dataframe
from core.utilities import construct_cluster_data


def generate_radar_data(f_radar_chart_features,
                              f_strongest_ico_data,
                              f_weakest_ico_data,
                              f_avg_dict, out_file_name):

    path = path_to_output + out_file_name
    file_name = open(path, "w+")
    no_features = len(f_radar_chart_features)
    i = 0
    print("""[""", file=file_name)
    for radar_chart_feature in f_radar_chart_features:
        print("""{\"feature\":\"""", radar_chart_feature, """\",""", file=file_name)
        v = f_strongest_ico_data[radar_chart_feature].iloc(0)[0]
        if v >=1:
            print("""\"Strongest\":""", round(log10(v), 2), """,""", file=file_name)
        else:
            print("""\"Strongest\": 0,""", file=file_name)

        v = f_weakest_ico_data[radar_chart_feature].iloc(0)[0]
        if v >=1:
            print("""\"Weakest\":""", round(log10(v), 2), """,""", file=file_name)
        else:
            print("""\"Weakest\": 0,""", file=file_name)
        v = f_avg_dict[radar_chart_feature]
        if v >= 1:
            print("""\"Average\":""", round(log10(v), 2), file=file_name)
        else:
            print("""\"Average\":0""", file=file_name)
        if i < no_features - 1:
            print("},", file=file_name)
        else:
            print("}", file=file_name)
        i += 1
    print("""]""", file=file_name)


def generate_regression_data(regression_dataframe, out_file_name):
    path = path_to_output + out_file_name
    file_name = open(path, "w+")

    result = regress_dataframe(regression_dataframe)
    print(result.summary(), file=file_name)


def generate_frontend_data(etl_raw_ico_data, ico_data_model, labels):
    file_path = path_to_output + ecosystems_clusters_file_name
    ico_ecosystem_file = open(file_path, "w+")

    print("""{\"name\": \"ICO Ecosystem\",\"children\": [""", file=ico_ecosystem_file)
    money_raised_max = 0
    money_raised_min = 10000000000

    avg_cluster_data = {}
    for radar_chart_feature in radar_chart_features:
        avg_cluster_data[radar_chart_feature] = 0

    no_icos = 0
    no_clusters = len(labels)
    consolidated_cluster_data = construct_cluster_data(etl_raw_ico_data, ico_data_model, labels)

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

            print("""{\"name\": \"""", row[1]['coin'], """\",\"loc\":""", row[1]['raised'], end='',
                  file=ico_ecosystem_file)

            if ix + 1 < len(cluster_data.index):
                print("},", file=ico_ecosystem_file)
            else:
                print("}", file=ico_ecosystem_file)
            ix += 1

        if c < no_clusters - 1:
            print("]},", file=ico_ecosystem_file)
        else:
            print("]}", file=ico_ecosystem_file)
    print("""]}""", file=ico_ecosystem_file)

    strongest_ico_data = consolidated_cluster_data[consolidated_cluster_data['coin'] == strongest_ico]
    weakest_ico_data = consolidated_cluster_data[consolidated_cluster_data['coin'] == weakest_ico]

    for radar_chart_feature in radar_chart_features:
        avg_cluster_data[radar_chart_feature] /= no_icos
        avg_cluster_data[radar_chart_feature] = round(avg_cluster_data[radar_chart_feature], 2)

    print("ICO CLUSTERS", labels)
    print("-----------------------------")
    print("Winning ICO:", strongest_ico_data)
    print("Weakest ICO:", weakest_ico_data)

    generate_radar_data(radar_chart_features, strongest_ico_data, weakest_ico_data, avg_cluster_data,
                        ecosystem_radar_file_name)
    generate_regression_data(consolidated_cluster_data, ecosystem_regression_file_name)

    generate_all_clusters_radar_data(consolidated_cluster_data, labels)
    return True


def generate_all_clusters_radar_data(consolidated_cluster_data, labels):

    for c in labels:
        no_icos = 0
        money_raised_max = 0
        money_raised_min = 10000000000
        avg_cluster_data = {}
        for radar_chart_feature in radar_chart_features:
            avg_cluster_data[radar_chart_feature] = 0

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

        strongest_ico_data = consolidated_cluster_data[consolidated_cluster_data['coin'] == strongest_ico]
        weakest_ico_data = consolidated_cluster_data[consolidated_cluster_data['coin'] == weakest_ico]

        for radar_chart_feature in radar_chart_features:
            avg_cluster_data[radar_chart_feature] /= no_icos
            avg_cluster_data[radar_chart_feature] = round(avg_cluster_data[radar_chart_feature], 2)

        print("ICO CLUSTER", str(c))
        print("-----------------------------")
        print("Winning ICO:", strongest_ico_data)
        print("Weakest ICO:", weakest_ico_data)

        current_file_name = "radar_cluster_"+str(c+1)+".json"
        generate_radar_data(radar_chart_features, strongest_ico_data, weakest_ico_data, avg_cluster_data, current_file_name)
        regression_file_name = "cluster_" + str(c + 1) + "_regression.out"
        generate_regression_data(cluster_data, regression_file_name)
