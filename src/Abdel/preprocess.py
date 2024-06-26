import pandas as pd

def preprocess(player_stats, line_ups):
    # Rename the column 'ID' to 'PlayerID'
    line_ups.rename(columns={'ID': 'PlayerID'}, inplace=True)

    # Merge the datasets on common columns (PlayerID and MatchID)
    merged_df = pd.merge(line_ups, player_stats, on=['PlayerID', 'MatchID'])
    
    # Remove the goalkeepers from the dataset for lack of relevant stats
    merged_df = merged_df[merged_df['Role'] != 'goalkeepers']

    # Filter the data for relevant stats
    relevant_stats = ['Recovered balls', 'Distance covered (Km)', 'Tackles won', 'Fouls committed']
    filtered_df = merged_df[merged_df['StatsName'].isin(relevant_stats)]
    
    # Set Value column to integer
    filtered_df['Value'] = filtered_df['Value'].astype('float64')

    # Group by Role and StatsName and sum the Value
    df_metrics = filtered_df.groupby(['Country', 'Role', 'StatsName'])['Value'].sum().reset_index()
    
    # Filter the data for relevant stats
    relevant_stats = ['Goals scored by left foot', 'Goals scored by right foot']
    filtered_df = merged_df[merged_df['StatsName'].isin(relevant_stats)]
    
    # Set Value column to integer
    filtered_df['Value'] = filtered_df['Value'].astype('float64')

    # Group by Role and StatsName and sum the Value (goals)
    df_foot = filtered_df.groupby(['Country', 'Role', 'StatsName'])['Value'].sum().reset_index()

    return df_metrics, df_foot