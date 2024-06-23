import pandas as pd

def preprocess_data(match_infos, player_stats, line_ups):
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

    # Calculate z-scores manually
    df['Temperature_mean'] = df.groupby('Country')['Temperature'].transform('mean')
    df['Temperature_std'] = df.groupby('Country')['Temperature'].transform('std')
    df['Temperature_zscore'] = (df['Temperature'] - df['Temperature_mean']) / df['Temperature_std']

    df['Humidity_mean'] = df.groupby('Country')['Humidity'].transform('mean')
    df['Humidity_std'] = df.groupby('Country')['Humidity'].transform('std')
    df['Humidity_zscore'] = (df['Humidity'] - df['Humidity_mean']) / df['Humidity_std']

    df['Average_zscore'] = (df['Temperature_zscore'] + df['Humidity_zscore']) / 2

    # Drop intermediate columns
    df.drop(['Temperature_mean', 'Temperature_std', 'Humidity_mean', 'Humidity_std'], axis=1, inplace=True)

    return df