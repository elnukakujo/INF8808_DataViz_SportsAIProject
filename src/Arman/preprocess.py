import pandas as pd

def min_max_scale(series):
    return (series - series.min()) / (series.max() - series.min())

def preprocess(match_stats):
    # Filter and process goals scored
    match_stats_goals = match_stats.loc[match_stats['StatsName'] == 'Goals scored', ['TeamName', 'Value']]
    match_stats_goals['Value'] = pd.to_numeric(match_stats_goals['Value'])
    match_stats_goals = match_stats_goals.groupby('TeamName')['Value'].mean().reset_index()
    match_stats_goals['Scaled Value Goals'] = min_max_scale(match_stats_goals['Value'])
    match_stats_goals.rename(columns={'Value': 'Average Goals Scored per Game'}, inplace=True)

    # Filter and process attempts accuracy
    match_stats_attempts = match_stats.loc[match_stats['StatsName'] == 'Attempts Accuracy', ['TeamName', 'Value']]
    match_stats_attempts['Value'] = pd.to_numeric(match_stats_attempts['Value']).div(100)
    match_stats_attempts = match_stats_attempts.groupby('TeamName')['Value'].mean().reset_index()
    match_stats_attempts.rename(columns={'Value': 'Average Attempts % Accuracy'}, inplace=True)

    # Filter and process passes accuracy
    match_stats_passes = match_stats.loc[match_stats['StatsName'] == 'Passes accuracy', ['TeamName', 'Value']]
    match_stats_passes['Value'] = pd.to_numeric(match_stats_passes['Value']).div(100)
    match_stats_passes = match_stats_passes.groupby('TeamName')['Value'].mean().reset_index()
    match_stats_passes.rename(columns={'Value': 'Average Passes Accuracy'}, inplace=True)

    # Filter and process fouls committed
    match_stats_fouls = match_stats.loc[match_stats['StatsName'] == 'Fouls committed', ['TeamName', 'Value']]
    match_stats_fouls['Value'] = pd.to_numeric(match_stats_fouls['Value'])
    match_stats_fouls = match_stats_fouls.groupby('TeamName')['Value'].mean().reset_index()
    match_stats_fouls['Scaled Value Fouls'] = min_max_scale(match_stats_fouls['Value'])
    match_stats_fouls.rename(columns={'Value': 'Average Fouls Committed per Game'}, inplace=True)

    # Filter and process ball possession
    match_stats_bp = match_stats.loc[match_stats['StatsName'] == 'Ball Possession', ['TeamName', 'Value']]
    match_stats_bp['Value'] = pd.to_numeric(match_stats_bp['Value']).div(100)
    match_stats_bp = match_stats_bp.groupby('TeamName')['Value'].mean().reset_index()
    match_stats_bp.rename(columns={'Value': 'Average Ball Possession % per Game'}, inplace=True)

    # Merge all processed statistics into a single DataFrame
    merged_stats = (
        match_stats_goals
        .merge(match_stats_attempts, on='TeamName')
        .merge(match_stats_passes, on='TeamName')
        .merge(match_stats_fouls, on='TeamName')
        .merge(match_stats_bp, on='TeamName')
    )

    return merged_stats