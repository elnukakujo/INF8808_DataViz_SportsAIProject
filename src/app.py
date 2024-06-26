import dash
from dash import html
from dash import dcc
from dash import Input, Output
import plotly.io as pio

from get_df import load_data
from Noe.preprocess import preprocess as noe_preprocess
from Noe.make_viz import create_scatter, create_stacked_bars
from Arman.preprocess import preprocess as arman_preprocess
from Arman.make_viz import create_radar_chart, add_team_to_radar_chart, create_empty_radar_chart
from khedrO.preprocess import preprocess_data
from khedrO.make_viz import create_figure
from Abdel.preprocess import preprocess as abdel_preprocess
from Abdel.make_viz import create_bars
from Amadeus.preprocess import preprocess as amadeus_preprocess
from Amadeus.make_viz import draw
from Ibrahima.preprocess import preprocess as ibrahima_preprocess
from Ibrahima.make_viz import create_bar_chart
from template import create_template

app = dash.Dash(__name__)
app.title = 'SportsAI Project'

create_template()
pio.templates.default = 'simple_white+mytemplate'

# Preprocess data
match_infos, match_stats, player_stats, line_ups = load_data()
data = noe_preprocess(match_infos, match_stats)
radar_data = arman_preprocess(match_stats)
bubble_data = preprocess_data(match_infos, player_stats, line_ups)
df_metrics, df_foot = abdel_preprocess(player_stats, line_ups)
df_amadeus = amadeus_preprocess(player_stats, line_ups)
df_ibrahima = ibrahima_preprocess(player_stats)


app.layout = html.Div([
    html.Div(className='section', id='intro', children=[
        html.H1('SportsAI'),
        html.H2('Boost your Players with Data'),
    ]),
    html.Div(className='section',id='about_us', children=[
        html.Div(className='content', children=[
            html.Div(className='description', children=[
                html.H3('About Us'),
                html.P(
                    "At SportsAI, we are dedicated to revolutionizing the way coaches enhance their players' " +
                    "performance through cutting-edge data visualization. Our team combines expertise in sports " +
                    "science and advanced analytics to provide insightful, actionable data that empowers coaches to " +
                    "make informed decisions. Whether it's tracking progress, identifying strengths and weaknesses, or " +
                    "optimizing training strategies, SportsAI is your partner in achieving peak performance. Join us and " +
                    "transform your data into a competitive edge."
                )
            ]),
            html.Div(className='img-container', children=[
                html.Img(src='assets/img/aboutus.jpg', alt='The Italian Team posing with the trophy after winning the Euro 2020'),
                html.A('Image Source',
                    href='https://www.nbcnews.com/news/world/italy-wins-european-soccer-championship-3-2-penalty-shootout-n1273643',
                    target='_blank')
            ])
        ])
    ]),
    html.Div(className='section',id='match_overview', children=[
        html.Div(className='content', children=[
            html.Div(className='description', children=[
                html.H3('Match Overview'),
                html.P(
                    "The first group of visualizations includes multiple graphics that illustrate various aspects of the matches. " +
                    "These visualizations are designed to address general questions you might have and to introduce you to " +
                    "our work. Specifically, we present:"
                ),
                html.Ol(children=[
                    html.Li(
                        "The number of goals scored and fouls committed in each match, under the assumption that the entertainment " +
                        "value of a game is correlated with the number of goals."
                    ),
                    html.Li(
                        "A comparison between the number of goals scored in open play and those scored from set pieces.")
                ]),
                html.P(
                    "These visualizations offer a comprehensive overview of key match statistics, enhancing the understanding " +
                    "of the factors that contribute to the dynamics of the game."
                ),
                html.P("Try hovering hover the elements in the graph and play with the legend to get more details!")
            ]),
            html.Div(id='scatter_bar_container',className='viz-container', children=[
                html.Label('Select a plot:'),
                dcc.Dropdown(
                    id='type-dropdown',
                    options=[{'label': 'Total Score vs Fouls for Matches', 'value': 'scatter'},
                            {'label': 'Goals Scored in Open Play vs Set Pieces', 'value': 'horizontal_bar'}],
                    value='scatter',
                    clearable=False
                ),
                dcc.Graph(
                    className='graph',
                    id='scatter_horizontal_bar'
                )
            ])
        ])
    ]),
    html.Div(className='section',id='radar_chart', children=[
        html.Div(className='content', children=[
            html.Div(className='description', children=[
                html.H3('Team Performance Radar Chart'),
                html.P(
                    "The radar chart compares various performance metrics across teams. The first team is defaulted to Italy, the winner of the tournament. Each axis represents a different statistic: "
                ),
                html.Ul([
                    html.Li("Goals Scored per Game: Average number of goals scored in each game. Note: This value is MinMax Scaled to [0,1] range."),
                    html.Li("Attempts Accuracy: Percentage of attempts on target."),
                    html.Li("Passes Accuracy: Percentage of successful passes."),
                    html.Li("Fouls Committed per Game: Average number of fouls committed per game. Note: This value is MinMax Scaled to [0,1] range."),
                    html.Li("Ball Possession % per Game: Average percentage of time the team has possession of the ball.")
                ])
            ])
        ]),
        html.Div(className='viz-container', children=[
            html.Label('Select First Team'),
            dcc.Dropdown(
                id='first-team-dropdown',
                options=[{'label': team, 'value': team} for team in radar_data['TeamName']],
                value='Italy'
            ),
            html.Label('Select Second Team'),
            dcc.Dropdown(
                id='second-team-dropdown',
                options=[{'label': team, 'value': team} for team in radar_data['TeamName']]
            ),
            dcc.Graph(
                id='radar1',
                className='graph',
                figure=create_radar_chart(radar_data, 'Italy')
            )
        ])
    ]),
    html.Div(className='section',id='weather_performance', children=[
        html.Div(className='content',children=[
            html.Div(className='description', children=[
                html.H3("Impact of Weather on Player Performance"),
                html.P(
                        "The bubble chart shows how meteorological conditions affect different players: "
                ),
                html.Ul([
                    html.Li("Each bubble represents the selected players performance for a match. The size of the bubble is proportional to the players' performance for the chosen statistic."),
                    html.Li("The color of the bubble indicates the average z-scores of temperature and humidity for the match in question. Where the Z-score defines how many standard deviations a data point is from the mean, and is calculated using the formula: 𝑍 = 𝑋 − 𝜇 / 𝜎"),
                    html.Li("Should there be no data for a particular player, for the chosen statistic, 'No data available.' will be displayed. For example, if you look at yellow cards, and the player has none."),
                    html.Li("Hover over the bubbles to obtain more detailed information. The value for the chosen statistic, the oppponent for the match in question, etc."),
                ]),
            ]),
            html.Div(className='viz-container', children=[
                html.Label('Select a Country'), 
                dcc.Dropdown(
                    id='country-dropdown',
                    options=[{'label': country, 'value': country} for country in bubble_data['Country'].unique()]
                ),
                html.Label('Select a Player'), 
                dcc.Dropdown(
                    id='player-dropdown'
                ),
                html.Label('Select a Statistic'), 
                dcc.Dropdown(
                    id='stat-dropdown',
                    options=[{'label': stat, 'value': stat} for stat in bubble_data['StatsName'].unique()]
                ),
                html.Div(id='output-container')
            ])
        ])
    ]),
    html.Div(className='section',id='peformance_metrics', children=[
        html.Div(className='content', children=[
            html.Div(className='description',children=[
                html.H3('Performance Metrics'),
                html.P(
                    "This bar chart provides a clear visual comparison of key performance metrics across different soccer player positions."+
                    " It allows for insightful analysis of how the roles and responsibilities of defenders, midfielders, forwards, and goalkeepers"+
                    " are reflected in their recovered balls, distance covered, tackles won, and fouls committed. This data visualization offers valuable"+
                    " insights into the distinct contributions of each position within a soccer team."
                ),
                html.P(
                    "The comprehensive nature of the data presented and the intuitive layout of the chart make it an effective tool for coaches, analysts,"+
                    " and fans to understand the nuanced differences in the playing styles and tactical responsibilities of various player positions. This"+
                    " type of visual analysis can inform strategic decisions and player development efforts."
                ),
            ]),
            html.Div(className='viz-container', children=[
                html.Label('Select a Country'), 
                dcc.Dropdown(
                    id='country-dropdown2',
                    options=[{'label': country, 'value': country} for country in df_metrics['Country'].unique()],
                    value='Italy'
                ),
                dcc.Graph(
                    className='graph',
                    id='bar1'
                )
            ])
        ])
    ]),
    html.Div(className='section',id='foot_analysis', children=[
        html.Div(className='content', children=[
            html.Div(className='description', children=[
                html.H3('Foot Analysis'),
                html.P(
                    "This bar chart provides a clear visualization of the number of goals scored by players in different positions "+
                    "(defenders, forwards, and midfielders) using their left and right feet. This data offers valuable insights into the "+
                    "preferred scoring tendencies and footedness of players in various roles. "
                ),
                html.P(
                    "The chart shows that forwards score significantly more goals with their right foot compared to their left, while defenders "+
                    "and midfielders exhibit a more balanced distribution of goals between their two feet. This information can help coaches and "+
                    "analysts understand the unique strengths and preferences of players in each position, informing training and tactical decisions. "
                ),
            ]),
            html.Div(className='viz-container', children=[
                html.Label('Select a Country'), 
                dcc.Dropdown(
                    id='country-dropdown3',
                    options=[{'label': country, 'value': country} for country in df_metrics['Country'].unique()],
                    value='Italy'
                ),
                dcc.Graph(
                    className='graph',
                    id='bar2'
                )
            ])
        ])
    ]),
    html.Div(className='section',id='stats_role', children=[
        html.Div(className='content', children=[
            html.Div(className='description', children=[
                html.H3('Player Stats by Role'),
                html.P(
                     "The following visualizations provide insights into the performance of players based on their roles during the tournament."+
                     "These metrics are crucial for evaluating player contributions and identifying key performers."+
                     "The visualizations include:"
                ), 
            ]),
            html.Div(className='viz-container', children=[
                html.Label('Select a plot:'),
                dcc.Dropdown(
                    id='plot-selector',
                    options=[
                        {'label': 'Contributions', 'value': 'contributions'},
                        {'label': 'Goals', 'value': 'goals'},
                        {'label': 'Assists', 'value': 'assists'}
                    ],
                    value='contributions',  # Default value
                    clearable=False
                ),
                dcc.Graph(
                    id='bar3',
                    className='graph'
                )
            ])
        ])
    ]),
    html.Div(className='section',id='tackles_bar', children=[
        html.Div(className='content', children=[
            html.H3('Tackles'),
            html.P(
                "This graph showcases the top 15 players by tackles won during Euro 2020, highlighting key defensive performances from various countries. "+
                "Leading the list are Kalvin Phillips (England), Stefan Lainer (Austria), and Marco Verratti (Italy), underscoring the crucial role of both "+
                "midfielders and defenders in regaining possession. The data indicates that teams with high tackle counts, such as Italy, England, and Denmark, "+
                "generally advanced far in the tournament, suggesting a strong link between aggressive defense and overall team success. This emphasizes the "+
                "importance of effective defensive play in achieving success at Euro 2020."
            ),
            html.Div(className='viz-container', children=[
                dcc.Graph(
                    figure=create_bar_chart(df_ibrahima),
                    className='graph',
                    id='tackles-bar'
                )
            ])
        ]),
    ])
])

# Callback for the match overview 
@app.callback(
    [Output('scatter_horizontal_bar','figure'),
     Output('scatter_bar_container','style')],
    Input('type-dropdown', 'value')
)
def update_graph(selected_type):
    if selected_type == 'scatter':
        return create_scatter(data), {'width': '700px', 'height': '600px'}
    if selected_type == 'horizontal_bar':
        return create_stacked_bars(data), {'width': '800px', 'height': '900px'}

# Callback for the radar chart
@app.callback(
    Output('radar1', 'figure'),
    Input('first-team-dropdown', 'value'),
    Input('second-team-dropdown', 'value')
)
def update_radar_chart(first_team, second_team):
    if first_team and second_team:
        radar_fig = create_radar_chart(radar_data, first_team)
        add_team_to_radar_chart(radar_fig, radar_data, second_team)
        return radar_fig
    elif not first_team and not second_team:
        return create_empty_radar_chart()
    elif not first_team:
        return create_radar_chart(radar_data, second_team)
    elif not second_team:
        return create_radar_chart(radar_data, first_team)

# Callbacks for the bubble chart
@app.callback(
    Output('output-container', 'children'),
    [Input('country-dropdown', 'value'),
     Input('player-dropdown', 'value'),
     Input('stat-dropdown', 'value')]
)
def update_figure(selected_country, selected_player, selected_stat):
    filtered_df = bubble_data[(bubble_data['Country'] == selected_country) &
                              (bubble_data['FullName'] == selected_player) &
                              (bubble_data['StatsName'] == selected_stat)]

    if filtered_df.empty:
        return html.Div("Select a Country, Player, and Statistic.",
                        style={'color': 'red', 'font-size': '20px', 'text-align': 'center', 'margin-top': '20px'})
    if (filtered_df['Value'] == 0).all():
        return html.Div("No data available.",
                        style={'color': 'red', 'font-size': '20px', 'text-align': 'center', 'margin-top': '20px'})

    return create_figure(filtered_df)

@app.callback(
Output('player-dropdown', 'options'),
Input('country-dropdown', 'value')
)
def update_player_dropdown(selected_country):
    if selected_country:
        players = bubble_data[bubble_data['Country'] == selected_country]['FullName'].dropna().unique()
        return [{'label': player, 'value': player} for player in players]
    return []

# Callback for Performance Metrics
@app.callback(
    Output('bar1', 'figure'),
    Input('country-dropdown2', 'value')
)
def update_graph(selected_country):
    return create_bars(
        df_metrics, 
        selected_country, 
        f'The values of Recovered balls, Distance covered (km), Tackles won, and Fouls committed by player positions for {selected_country}'
    )

# Callback for Foot Analysis
@app.callback(
    Output('bar2', 'figure'),
    Input('country-dropdown3', 'value')
)
def update_graph(selected_country):
    return create_bars(
        df_foot, 
        selected_country, 
        f'Number of Goals Scored by Left and Right Foot by Player Position for {selected_country}'
    )

# Callback for Player Stats by Role
@app.callback(
    Output('bar3', 'figure'),
    Input('plot-selector', 'value')
)
def update_graph(selected_plot):
    return draw(selected_plot,df_amadeus)

server = app.server
