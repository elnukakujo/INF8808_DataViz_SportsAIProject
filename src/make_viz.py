'''
    Draw the figures 
'''
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def create_bar(df, y, customdata, hovertemplate):
    fig=go.Figure()
    for team in df['HomeTeamName'].unique():
        team_df=df.loc[df.HomeTeamName==team]
        fig.add_trace(
            go.Bar(
                name=team,
                x=team_df['MatchName'],
                y=team_df[y],
                customdata=np.stack((team_df[customdata[0]],team_df[customdata[1]].str[0],team_df[customdata[1]].str[1]), axis=-1),
                hovertemplate=hovertemplate(y)
            )
        )
    fig.update_layout(
        barmode='group',
        template="simple_white",
        yaxis=dict(
            title=y,
            dtick=2
        ),
        xaxis=dict(
            tickangle=-45
        )
    )
    return fig

def create_bubble(df, x, y, customdata, hovertemplate):
    fig=px.scatter(df, x=x,y=y,color=customdata[1],custom_data=[df[customdata[0]],df[customdata[1]]])
    fig.update_traces(marker_size=15,hovertemplate=hovertemplate)
    fig = fig.update_layout(
        template="simple_white"
    )
    return fig

def create_stacked_bars(df, y, customdata, hovertemplate):
    stacked_bars=go.Figure()
    
    for mode in y:
        stacked_bars.add_trace(
            go.Bar(
                name=mode,
                x=df['MatchName'],
                y=df[mode],
                hovertemplate=hovertemplate(mode),
                customdata=df[customdata]
            )
        )
    stacked_bars.update_yaxes(range=[0,8])
    stacked_bars.update_layout(
        barmode='relative',
        template="simple_white",
        yaxis=dict(
            title='Number of Goals'
        ),
        xaxis=dict(
            tickangle=-45
        )
    )
    return stacked_bars