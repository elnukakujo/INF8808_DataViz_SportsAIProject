# khedrO/make_viz.py
import plotly.express as px
from dash import dcc, html

def create_visualization(df):
    unique_stats = df['StatsName'].unique()

    app_layout = html.Div([
        html.H3("Impact of Weather on Player Performance"),
        ##Added block to explain the figure, and follow format of other interactive dash viz::
        html.P(
                "The bubble chart shows how meteorological conditions affect different players: "
                ),
                html.Ul([
                    html.Li("Each bubble represents the selected players performance for a match. The size of the bubble is proportional to the players' performance for the chosen statistic."),
                    html.Li("The color of the bubble indicates the average z-scores of temperature and humidity for the match in question."),
                    html.Li("Should there be no data for a particular player, for the chosen statistic, 'No data available.' will be displayed. For example, if you look at yellow cards, and the player has none"),
                    html.Li("Hover over the bubbles to obtain more detailed information. The value for the chosen statistic, the oppponent for the match in question, etc."),
                ]),
        ##
        html.Label('Select a Country'), #added
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in df['Country'].unique()]
        ),
        html.Label('Select a Player'), #added
        dcc.Dropdown(
            id='player-dropdown'
        ),
        html.Label('Select a Statistic'), #added
        dcc.Dropdown(
            id='stat-dropdown',
            options=[{'label': stat, 'value': stat} for stat in unique_stats]
        ),
        html.Div(id='output-container')
    ])

    return app_layout

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

    return dcc.Graph(figure=fig)
