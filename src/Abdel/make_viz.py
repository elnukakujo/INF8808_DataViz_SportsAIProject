import plotly.express as px

def create_bars(df,country, title):
    country_df = df[df['Country'] == country]
    fig = px.bar(country_df, x='StatsName', y='Value', color='Role', barmode='group',
                 labels={'Value': 'Value', 'Role': 'Player Position'},
                 title=title)
    return fig