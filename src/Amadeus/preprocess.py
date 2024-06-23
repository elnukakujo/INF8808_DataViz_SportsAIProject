import pandas as pd

def preprocess(df,df_2):
    df = df[df["StatsName"].isin(["Goals", "Assists"])]
    df = df[['FullName', 'StatsName', 'Value']]
    df['Value'] = df['Value'].astype(int)
    df_grouped = df.groupby(['FullName', 'StatsName'])['Value'].sum().unstack(fill_value=0).reset_index()
    # Keep full name and role without duplicates
    
    df_2 = df_2.drop_duplicates(subset=['FullName'])

    df_grouped["Role"]=0
    df_grouped["Role"] = df_grouped["FullName"].map(df_2.set_index("FullName")["Role"])

    df_grouped["Total Contributions"]=df_grouped["Goals"]+df_grouped["Assists"]
    df_grouped=df_grouped[df_grouped["Role"].isin(["forwards","midfielders","defenders","goalkeepers"])]

    return df_grouped