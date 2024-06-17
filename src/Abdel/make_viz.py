import plotly.express as px

def create_bars(df1,df2):
    fig1 = px.bar(df1, x='Role', y='Value', color='StatsName', barmode='group',
                labels={'Value': 'Value', 'Role': 'Player Position'},
                title= 'The values of Recovered balls, Distance covered (KM), Tackles won, and Fouls committed by Player Position')

    fig2 = px.bar(df2, x='Role', y='Value', color='StatsName', barmode='group',
                labels={'Value': 'Number of Goals', 'Role': 'Player Position'},
                title='Number of Goals Scored by Left Foot and Right Foot by Player Position')
    return fig1,fig2