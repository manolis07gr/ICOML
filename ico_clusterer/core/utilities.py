import pandas as pd
from math import log10


def construct_cluster_data(raw_ico_data, clusters):
    consolidated_cluster_data = pd.DataFrame()
    for c in clusters:
        cluster_data = raw_ico_data[raw_ico_data['cluster'] == c]
        consolidated_cluster_data = consolidated_cluster_data.append(cluster_data)
    return consolidated_cluster_data


def export_cluster_radar_json(f_radar_chart_features,
                              f_strongest_ico_data,
                              f_weakest_ico_data,
                              f_avg_dict):

    no_features = len(f_radar_chart_features)
    i = 0
    print("""[""", file=open("output.txt", "w"))
    for radar_chart_feature in f_radar_chart_features:
        print("""{\"feature\":\"""", radar_chart_feature, """\",""", file=open("output.txt", "a"))
        v = f_strongest_ico_data[radar_chart_feature].iloc(0)[0]
        if v >=1:
            print("""\"Strongest\":""", round(log10(v), 2), """,""", file=open("output.txt", "a"))
        else:
            print("""\"Strongest\": 0,""", file=open("output.txt", "a"))

        v = f_weakest_ico_data[radar_chart_feature].iloc(0)[0]
        if v >=1:
            print("""\"Weakest\":""", round(log10(v), 2), """,""", file=open("output.txt", "a"))
        else:
            print("""\"Weakest\": 0,""", file=open("output.txt", "a"))
        v = f_avg_dict[radar_chart_feature]
        if v >= 1:
            print("""\"Average\":""", round(log10(v), 2), file=open("output.txt", "a"))
        else:
            print("""\"Average\":0""", file=open("output.txt", "a"))
        if i < no_features - 1:
            print("},", file=open("output.txt", "a"))
        else:
            print("}", file=open("output.txt", "a"))
        i += 1
    print("""]""", file=open("output.txt", "a"))
