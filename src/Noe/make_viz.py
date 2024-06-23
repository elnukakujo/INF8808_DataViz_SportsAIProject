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
            text='Total Scores vs Total Fouls for Euro 2020 Matches' 
        ),
        legend=dict(
            title=dict(
                text='Rounds',
            )
        ),
        xaxis=dict(
            title='Total Scores',
            range=[-1, 9]
        ),
        yaxis=dict( 
            title='Total Fouls',
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
        barmode='stack',
        title=dict(
            text='Goals by Match (Horizontal Bar Chart)'
        ),
        legend=dict(
            title=dict(
                text='Types of Goals'
            )
        ),
        xaxis=dict(
            title='Number of Goals',
            range=[0, 8]
        ),
        yaxis=dict(
            title='Match',
            autorange="reversed"
        ),
        dragmode=False
    )
    return fig