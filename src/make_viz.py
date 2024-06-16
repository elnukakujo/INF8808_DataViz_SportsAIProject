'''
    Draw the figures 
'''
import plotly.graph_objects as go

def create_scatter(df, hovertemplate):
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
            hovertemplate=hovertemplate,
            customdata=group[['RoundName', 'MatchName']].values.tolist()
        )
        traces.append(trace)

    # Create a figure with all traces
    fig = go.Figure(data=traces)
    fig.update_layout(
        title='Total Scores vs Total Fouls for Euro 2020 Matches',
        xaxis_title='Total Scores',
        yaxis_title='Total Fouls',
        template="simple_white",
        showlegend=True,
        legend=dict(
            title='Rounds',
        ),
        xaxis=dict(range=[-1, 9]),  # Adjust range as per your data
        yaxis=dict(range=[-1, 39])
    )
    return fig

def create_stacked_bars(df, hovertemplate):
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
        hovertemplate=hovertemplate('Goals Open Play')
    ))

    fig.add_trace(go.Bar(
        y=df['MatchName'],
        x=df['GoalsSetPieces'],
        name='Goals Set Pieces',
        orientation='h',
        customdata=df['RoundName'],
        hovertemplate=hovertemplate('Goals Set Pieces')
    ))

    fig.update_layout(
        template='simple_white',
        barmode='stack',
        title='Goals by Match (Horizontal Bar Chart)',
        xaxis_title='Number of Goals',
        yaxis_title='Match',
        legend_title='Types of Goals',
        yaxis=dict(autorange="reversed"),
        height=1000,
        xaxis=dict(range=[0, 8]),  # Adjust range as per your data
    )
    return fig