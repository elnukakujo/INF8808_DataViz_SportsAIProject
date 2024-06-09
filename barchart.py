import plotly.express as px
import pandas as pd
import numpy as np
import hovertemplate as hover
import plotly.io as pio
import plotly.subplots
import template

def get_match_df(sheet_name=list(str), columns=dict()):
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
    stats_df = match_stats.loc[:,columns][(match_stats['StatsName'] == 'Fouls committed')]
    stats_df.loc[len(stats_df.index)] = [2024469, 'Fools committed', 0] #There is a hole in the data for MatchID 2024469, ze set it at 0 since we need to convert the element as int
    return stats_df.sort_values('MatchID').set_index(['MatchID']) #Sort the columns by MatchID and put it as index

def get_df(sheet_names, columns):
    match_df=get_match_df(sheet_names[0], columns[sheet_names[0]])
    stats_df = get_stats_df(sheet_names[1], columns[sheet_names[1]])

    match_df['FoolsCommitted']=stats_df.groupby('MatchID')['Value'].apply(list).tolist() #We add the FoolsCommitted in the match_df
    match_df['TotalFools']=match_df.FoolsCommitted.apply(lambda x: sum(x)).astype(int) #We create the TotalFools columns for the later y axis
    match_df=match_df.reset_index(drop=True)
    
    return match_df

def preprocess(sheet_names, columns):
    df = get_df(sheet_names, columns)
    
    df['MatchName']=df['HomeTeamName']+' vs '+df['AwayTeamName']
    df= df.drop(['HomeTeamName','AwayTeamName'], axis=1)
    
    df['TotalScore']=df['ScoreHome']+df['ScoreAway']
    df['RoundName']=df['RoundName'].str.title()
    
    df= df.drop(['ScoreHome','ScoreAway'], axis=1)
    return df

def draw(fig, df, axis_names, row):
    if axis_names[1]=='TotalScore':
        bars = px.bar(df,x=axis_names[0],y=axis_names[1], custom_data=['RoundName'], color='MatchName').data
        for bar in bars:
            bar['width']=1
            bar['hovertemplate']=hover.get_score_hover_template()
            bar['showlegend']=True
            fig.add_trace(bar, row=row, col=1)
    elif axis_names[1]=='TotalFools':
        bars = px.bar(df,x=axis_names[0],y=axis_names[1], custom_data=['RoundName','FoolsCommitted'], color='MatchName').data
        for bar in bars:
            bar['width']=1
            bar['hovertemplate']=hover.get_fools_hover_template()
            bar['showlegend']=False
            fig.add_trace(bar, row=row, col=1)
    return fig

sheet_names=['Match information','Match Stats']
columns={'Match information':['MatchID','HomeTeamName','AwayTeamName', 'RoundName','ScoreHome','ScoreAway'],
         'Match Stats':['MatchID','StatsName', 'Value']}

template.create_template()
pio.templates.default = 'simple_white+mytemplate'

df = preprocess(sheet_names, columns)
fig = plotly.subplots.make_subplots(rows=2,cols=1)
draw(fig, df, ['MatchName','TotalScore'],1)
draw(fig, df, ['MatchName','TotalFools'],2)
fig.update_xaxes(visible=False)
fig.show()