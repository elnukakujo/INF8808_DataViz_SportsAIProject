import pandas as pd

def get_df():
    #Reading the excel files
    play_stat=pd.read_excel("assets/data/EURO_2020_DATA.xlsx",sheet_name="Players stats")

    line_ups=pd.read_excel("assets/data/EURO_2020_DATA.xlsx",sheet_name="Line-ups")

    # Rename the column 'ID' to 'PlayerID'
    line_ups.rename(columns={'ID': 'PlayerID'}, inplace=True)

    # Merge the datasets on common columns (PlayerID and MatchID)
    merged_df = pd.merge(line_ups, play_stat, on=['PlayerID', 'MatchID'])

    # Filter the data for relevant stats
    relevant_stats = ['Recovered balls', 'Distance covered (Km)', 'Tackles won', 'Fouls committed']
    filtered_df = merged_df[merged_df['StatsName'].isin(relevant_stats)]
    # Group by Role and StatsName and sum the Value
    df1 = filtered_df.groupby(['Role', 'StatsName'])['Value'].sum().reset_index()
    
    relevant_stats = ['Goals scored by left foot', 'Goals scored by right foot']
    filtered_df = merged_df[merged_df['StatsName'].isin(relevant_stats)]
    # Group by Role and StatsName and sum the Value (goals)
    df2 = filtered_df.groupby(['Role', 'StatsName'])['Value'].sum().reset_index()

    return df1, df2