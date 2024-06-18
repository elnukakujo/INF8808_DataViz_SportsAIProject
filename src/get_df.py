import pandas as pd

def get_df(sheet_name):
    return pd.read_csv(f"./assets/data/EURO_2020_DATA_{sheet_name}.csv")