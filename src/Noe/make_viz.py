'''
    Draw the figures 
'''
import plotly.graph_objects as go
import Noe.hovertemplate as hover

def create_scatter(df):
    round_colors = {'Final Tournament': 'blue',
        'Eighth Finals': 'green',
        'Quarter Finals': 'orange',
        'Semi Finals': 'red',
        'Final': 'purple'
    }
    fig = go.Figure()
    
    df=df.sort_values('RoundName')
    
    traces = []
    
    for round_name, group in df.groupby('RoundName'):
        trace = go.Scatter(
            x=group['TotalScore'],
            y=group['TotalFouls'],
            mode='markers',
            marker=dict(color=round_colors[round_name], size=12),
            name=round_name,
            hovertemplate=hover.get_scatter_hover_template(),
            customdata=group[['RoundName', 'MatchName']].values.tolist()
        )
        traces.append(trace)

    # Create a figure with all traces
    fig = go.Figure(data=traces)
    fig.update_layout(
        title=dict(
            text='Total Scores vs Total Fouls for Euro 2020 Matches',
            font_size=16,
            font_family='Montserrat-Medium'    
        ),
        template="simple_white",
        legend=dict(
            title=dict(
                text='Rounds',
                font_size=14,
                font_family='Montserrat-Medium'
            ),
            font=dict(
                size=12,
                family='Roboto-Light'
            )
        ),
        xaxis=dict(
            title='Total Scores',
            titlefont=dict(
                size=14,
                family='Montserrat-Medium'
            ),
            tickfont=dict(
                size=12,
                family='Roboto-Light'
            ),
            range=[-1, 9]
        ),
        yaxis=dict( 
            title='Total Fouls',
            titlefont=dict(
                size=14,
                family='Montserrat-Medium'
            ),
            tickfont=dict(
                size=12,
                family='Roboto-Light'
            ),
            range=[-1, 39]
        ),
        dragmode=False
    )
    return fig

def create_stacked_bars(df):
    df['TotalGoals'] = df['GoalsOpenPlay'] + df['GoalsSetPieces']
    
    # Sort DataFrame by TotalGoals in descending order
    df = df.sort_values(by='TotalGoals', ascending=False)
    
    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=df['MatchName'],
        x=df['GoalsOpenPlay'],
        name='Goals Open Play',
        orientation='h',
        customdata=df['RoundName'],
        hovertemplate=hover.get_stacked_bar_hover_template('Goals Open Play')
    ))

    fig.add_trace(go.Bar(
        y=df['MatchName'],
        x=df['GoalsSetPieces'],
        name='Goals Set Pieces',
        orientation='h',
        customdata=df['RoundName'],
        hovertemplate=hover.get_stacked_bar_hover_template('Goals Set Pieces')
    ))

    fig.update_layout(
        template='simple_white',
        barmode='stack',
        title=dict(
            text='Goals by Match (Horizontal Bar Chart)', 
            font_size=16,
            font_family='Montserrat-Medium'
        ),
        xaxis_title='Number of Goals',
        yaxis_title='Match',
        legend=dict(
            title=dict(
                text='Types of Goals',
                font_size=14,
                font_family='Montserrat-Medium'
            ),
            font=dict(
                size=11,
                family='Roboto-Light'
            )
        ),
        xaxis=dict(
            titlefont=dict(
                size=14,
                family='Montserrat-Medium'
            ),
            tickfont=dict(
                size=11,
                family='Roboto-Light'
            ),
            range=[0, 8]
        ),
        yaxis=dict( 
            titlefont=dict(
                size=14,
                family='Montserrat-Medium'
            ),
            tickfont=dict(
                size=11,
                family='Roboto-Light'
            ),
            autorange="reversed"
        ),
        dragmode=False
    )
    return fig