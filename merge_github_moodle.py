# This script merges the github moodle csv file with the github classroom one. 
import pandas as pd

moodle_csv = pd.read_csv("./data/INF1007-L04-PR01.csv")
moodle_csv.drop(columns=["Unnamed: 0.2", "Unnamed: 0.1", "Unnamed: 0"], inplace=True)
classroom_csv = pd.read_csv("ghc.csv")
moodle_csv.reset_index(drop=True, inplace=True)
classroom_csv.reset_index(drop=True, inplace=True)
classroom_csv["Nom de famille"] = classroom_csv["roster_identifier"].apply(lambda x: x.split(",")[0])
classroom_csv["Prénom"] = classroom_csv["roster_identifier"].apply(lambda x: x.split(",")[1])
classroom_csv["TP3 repository"] = classroom_csv["student_repository_name"]
classroom_csv = classroom_csv[["Nom de famille", "github_username", "TP3 repository", "group_name"]]

combined_df = pd.merge(classroom_csv, moodle_csv, on="Nom de famille", how="outer")
combined_df.to_csv("./test-students.csv", index=False)