import pandas as pd

def get_df(sheet_name):
    data = pd.read_csv(f"./assets/data/EURO_2020_DATA_{sheet_name}.csv")
    if sheet_name == "Players_stats":
        data["FullName"] = data["PlayerName"] + " " + data["PlayerSurname"]
        return data
    elif sheet_name == "Line-ups":
        data["FullName"] = data["OfficialName"] + " " + data["OfficialSurname"]
        return data
    else:
        return data