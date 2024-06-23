import plotly.express as px
from dash import dcc

def create_figure(filtered_df):
    fig = px.scatter(
        filtered_df,
        x="Temperature",
        y="Humidity",
        size="Value",
        color="Average_zscore",
        hover_data={'Temperature': True, 'Humidity': True, 'Value': True, 'Opponent': True},
        size_max=60,
        custom_data=['Opponent']
    )

    fig.update_traces(hovertemplate="<br>".join([
        "Temperature: %{x}",
        "Humidity: %{y}",
        "Value: %{marker.size}",
        "Opponent: %{customdata[0]}"
    ]))

    return dcc.Graph(figure=fig, className="graph", id="bubble1")