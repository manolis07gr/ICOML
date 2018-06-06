import pandas as pd
from math import log10
import statsmodels.formula.api as sm

def construct_cluster_data(raw_ico_data, clusters):
    consolidated_cluster_data = pd.DataFrame()
    for c in clusters:
        cluster_data = raw_ico_data[raw_ico_data['cluster'] == c]
        consolidated_cluster_data = consolidated_cluster_data.append(cluster_data)
    return consolidated_cluster_data


def export_cluster_radar_json(f_radar_chart_features,
                              f_strongest_ico_data,
                              f_weakest_ico_data,
                              f_avg_dict, out_file_name):

    path= "./output/" + out_file_name
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


def export_cluster_regression(frame, out_file_name):
    path = "./output/" + out_file_name
    file_name = open(path, "w+")

    result = sm.ols(formula="raised ~ age + team", data=frame).fit()
    print(result.summary(), file=file_name)
