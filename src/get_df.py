import pandas as pd

def get_df(sheet_name):
    return pd.read_excel('assets/data/EURO_2020_DATA.xlsx', sheet_name=sheet_name)