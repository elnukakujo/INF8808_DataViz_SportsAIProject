import pandas as pd

def min_max_scale(series):
    return (series - series.min()) / (series.max() - series.min())
def preprocess(match_stats):
    match_stats_goals = match_stats[['MatchID', 'TeamName', 'StatsName', 'Value']]
    match_stats_goals = match_stats_goals.loc[match_stats_goals['StatsName'] == 'Goals scored']
    match_stats_goals.drop(['MatchID', 'StatsName'], axis=1, inplace=True)
    match_stats_goals['Value'] = pd.to_numeric(match_stats_goals['Value'])
    match_stats_goals = match_stats_goals.groupby(['TeamName']).mean().reset_index()

    match_stats_goals['Scaled Value Goals'] = min_max_scale(match_stats_goals['Value'])
    match_stats_goals.rename(columns={'Value': 'Average Goals Scored per Game'}, inplace=True)

    match_stats_attempts = match_stats[['MatchID', 'TeamName', 'StatsName', 'Value']]
    match_stats_attempts = match_stats_attempts.loc[match_stats_attempts['StatsName'] == 'Attempts Accuracy']
    match_stats_attempts.drop(['MatchID', 'StatsName'], axis=1, inplace=True)
    match_stats_attempts['Value'] = pd.to_numeric(match_stats_attempts['Value']).div(100)
    match_stats_attempts = match_stats_attempts.groupby(['TeamName']).mean().reset_index()

    match_stats_attempts.rename(columns={'Value': 'Average Attempts % Accuracy'}, inplace=True)

    match_stats_passes = match_stats[['MatchID', 'TeamName', 'StatsName', 'Value']]
    match_stats_passes = match_stats_passes.loc[match_stats_passes['StatsName'] == 'Passes accuracy']
    match_stats_passes.drop(['MatchID', 'StatsName'], axis=1, inplace=True)
    match_stats_passes['Value'] = pd.to_numeric(match_stats_passes['Value']).div(100)
    match_stats_passes = match_stats_passes.groupby(['TeamName']).mean().reset_index()

    match_stats_passes.rename(columns={'Value': 'Average Passes Accuracy'}, inplace=True)

    match_stats_fouls = match_stats[['MatchID', 'TeamName', 'StatsName', 'Value']]
    match_stats_fouls = match_stats_fouls.loc[match_stats_fouls['StatsName'] == 'Fouls committed']
    match_stats_fouls.drop(['MatchID', 'StatsName'], axis=1, inplace=True)
    match_stats_fouls['Value'] = pd.to_numeric(match_stats_fouls['Value'])
    match_stats_fouls = match_stats_fouls.groupby(['TeamName']).mean().reset_index()

    match_stats_fouls['Scaled Value Fouls'] = min_max_scale(match_stats_fouls['Value'])
    match_stats_fouls.rename(columns={'Value': 'Average Fouls Commited per Game'}, inplace=True)

    match_stats_bp = match_stats[['MatchID', 'TeamName', 'StatsName', 'Value']]
    match_stats_bp = match_stats_bp.loc[match_stats_bp['StatsName'] == 'Ball Possession']
    match_stats_bp.drop(['MatchID', 'StatsName'], axis=1, inplace=True)
    match_stats_bp['Value'] = pd.to_numeric(match_stats_bp['Value']).div(100)
    match_stats_bp = match_stats_bp.groupby(['TeamName']).mean().reset_index()

    match_stats_bp.rename(columns={'Value': 'Average Ball Possession % per Game'}, inplace=True)

    merged_stats = match_stats_goals.merge(match_stats_attempts, on='TeamName') \
        .merge(match_stats_passes, on='TeamName') \
        .merge(match_stats_fouls, on='TeamName') \
        .merge(match_stats_bp, on='TeamName')

    return merged_stats