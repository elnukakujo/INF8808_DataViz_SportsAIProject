'''
    Define the preprocess functions related to the excel data
'''

import pandas as pd

def get_match_df(sheet_name, columns):
    '''
        Returns the dataframe from the Match information sheet with only the wanted columns

        Args:
            sheet_name: The name of the sheet we want in the excel table
            street_df: The name of the columns we want in this sheet
        Returns:
            The dataframe from the Match information sheet with only the wanted columns

    '''
    match_infos = pd.read_excel('EURO_2020_DATA.xlsx', sheet_name=sheet_name)
    return match_infos.loc[:,columns].sort_values('MatchID').set_index(['MatchID']) #Takes only the columns we want, sort them by MatchID and put it as index

def get_stats_df(sheet_name, columns):
    match_stats = pd.read_excel('EURO_2020_DATA.xlsx', sheet_name=sheet_name)
    stats_df = match_stats.loc[:,columns][(match_stats['StatsName'] == 'Fouls committed')|(match_stats['StatsName'] == 'Goals scored')|(match_stats['StatsName'] == 'Goals scored in open play')]
    
    #There is holes in the data for some StatsName, we set it at 0 since we need to convert the element as int
    stats_df.loc[len(stats_df.index)] = [2024460, 'Goals scored in open play', 0]
    stats_df.loc[len(stats_df.index)] = [2024469, 'Fouls committed', 0] 
    stats_df.loc[len(stats_df.index)] = [2024469, 'Goals scored', 0]
    stats_df.loc[len(stats_df.index)] = [2024469, 'Goals scored in open play', 0]
    return stats_df.sort_values('MatchID').set_index(['MatchID']) #Sort the columns by MatchID and put it as index

def get_df(sheet_names, columns):
    match_df=get_match_df(sheet_names[0], columns[sheet_names[0]])
    stats_df=get_stats_df(sheet_names[1], columns[sheet_names[1]])
    stats_df=stats_df.groupby(by=['MatchID','StatsName'])['Value'].apply(list).reset_index()
    
    match_df['FoulsCommitted']=stats_df.loc[stats_df['StatsName']=='Fouls committed']['Value'].tolist() # We add the FoolsCommitted in the match_df
    match_df['TotalFouls']=match_df.FoulsCommitted.apply(lambda x: sum(x)).astype(int) #We create the TotalFools columns for the later y axis
    
    match_df['GoalsOpenPlay']=[sum(goals) for goals in stats_df.loc[stats_df['StatsName']=='Goals scored in open play']['Value']] # We sum and add the GoalsOpenPlay in the match_df
    
    match_df['GoalsSetPieces']=[sum(goals) for goals in stats_df.loc[stats_df['StatsName']=='Goals scored']['Value']]
    match_df['GoalsSetPieces']=match_df['GoalsSetPieces']-match_df['GoalsOpenPlay'] 
    # We sum and add the Goals of the matches and substract the GOalsOpenPlay to get the GoalsSetPieces in the match_df
    
    match_df=match_df.reset_index(drop=True)
    return match_df

def preprocess(sheet_names, columns):
    df = get_df(sheet_names, columns)
    
    df['MatchName']=df['HomeTeamName']+' vs '+df['AwayTeamName']
    df= df.drop(['AwayTeamName'], axis=1)
    
    df['TotalScore']=df['ScoreHome']+df['ScoreAway']
    df['TeamScore']=pd.Series(zip(df["ScoreHome"], df["ScoreAway"])).map(list)
    df['RoundName']=df['RoundName'].str.title()
    
    df= df.drop(['ScoreHome','ScoreAway'], axis=1)
    return df