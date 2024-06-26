import plotly.express as px

def create_bar_chart(data):
    fig = px.bar(data, x='FullName', y='Value', title="Top 15 Players by Tackles Won", 
                 color='FullName', # Use 'Player' column to differentiate colors
                 color_discrete_sequence=px.colors.qualitative.Plotly) # Different color for each bar
    fig.update_layout(
        title={'text': "Top 15 Players by Tackles Won", 'x': 0.5, 'xanchor': 'center'},
        bargap=0.4, # This makes the bars thinner
        legend=dict(
            title=dict(
                text="Player's Name"
            )
        ),
        xaxis=dict(
            title="Player's Name"
        ),
        yaxis=dict(
            title='Tackles Won'
        ),
        dragmode=False
    )
    return fig