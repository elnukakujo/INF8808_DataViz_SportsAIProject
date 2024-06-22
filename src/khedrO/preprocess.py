# khedrO/preprocess.py
import pandas as pd
from scipy.stats import zscore

def preprocess_data(match_infos, player_stats, line_ups):
    # Create a FullName column to facilitate plotting
    player_stats["FullName"] = player_stats["PlayerName"] + " " + player_stats["PlayerSurname"]
    line_ups["FullName"] = line_ups["OfficialName"] + " " + line_ups["OfficialSurname"]

    # Merge data
    df = pd.merge(player_stats, match_infos[['MatchID', 'Temperature', 'Humidity']], on=['MatchID'], how='inner')
    df = pd.merge(df, line_ups[['MatchID', 'Country', 'FullName']], on=['MatchID', 'FullName'], how='inner')

    # Add Opponent column
    def get_opponent(row):
        if row['HomeTeamName'] == row['Country']:
            return row['AwayTeamName']
        else:
            return row['HomeTeamName']

    df['Opponent'] = df.apply(get_opponent, axis=1)

    # Filter and clean data
    unique_stats = [
        "Goals", "Total Attempts", "Attempts on target", "Attempts off target",
        "Corners", "Offsides",
        "Saves", "Tackles won", "Clearances", "Recovered balls", "Fouls committed",
        "Yellow cards", "Red cards", "Passes completed", "Passes accuracy",
        "Distance covered (m)", "Distance covered in possession (m)",
        "Top Speed (Km/h)", "Own-goals", "Goals conceded"
    ]

    df = df[df['StatsName'].isin(unique_stats)]
    df = df[['Temperature', 'Humidity', 'Value', 'Opponent', 'Country', 'StatsName', 'FullName']]

    # Convert 'Value' column to numeric and drop NaN values
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    df = df.dropna(subset=['Value', 'Country'])

    # Calculate z-scores
    df['Temperature_zscore'] = zscore(df['Temperature'])
    df['Humidity_zscore'] = zscore(df['Humidity'])
    df['Average_zscore'] = (df['Temperature_zscore'] + df['Humidity_zscore']) / 2

    return df
