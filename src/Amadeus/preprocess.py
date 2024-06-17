import pandas as pd

def preprocess(df,df_2):
    df["FullName"]=df["PlayerName"]+" "+df["PlayerSurname"]
    df.drop(["PlayerName","PlayerSurname"],axis=1,inplace=True)

    df = df[df["StatsName"].isin(["Goals", "Assists"])]
    df = df[['FullName', 'StatsName', 'Value']]
    df['Value'] = df['Value'].astype(int)
    df_grouped = df.groupby(['FullName', 'StatsName'])['Value'].sum().unstack(fill_value=0).reset_index()

    df_2["FullName"]=df_2["OfficialName"]+" "+df_2["OfficialSurname"]
    # Keep full name and role without duplicates
    df_2 = df_2.drop_duplicates(subset=['FullName'])

    if df_2["FullName"].duplicated().any():
        raise ValueError("FullName column in df_2 has duplicate values. Ensure it is unique before proceeding.")

    df_grouped["Role"]=0
    df_grouped["Role"] = df_grouped["FullName"].map(df_2.set_index("FullName")["Role"])

    df_grouped["Total Contributions"]=df_grouped["Goals"]+df_grouped["Assists"]
    df_grouped=df_grouped[df_grouped["Role"].isin(["forwards","midfielders","defenders","goalkeepers"])]
    grouped_2=df_grouped.groupby("Role")["Total Contributions"].sum().sort_values(ascending=False)
    grouped_2_goal=df_grouped.groupby("Role")["Goals"].sum().sort_values(ascending=False)
    grouped_2_assist=df_grouped.groupby("Role")["Assists"].sum().sort_values(ascending=False)

    return grouped_2, grouped_2_goal, grouped_2_assist