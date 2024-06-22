import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.io as pio
from dash import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)
app.title = 'SportsAI Project'

import get_df

match_infos = get_df.get_df('Match_information')
match_stats = get_df.get_df('Match_Stats')
player_stats = get_df.get_df('Players_stats')
line_ups = get_df.get_df('Line-ups')

pio.templates.default = 'simple_white'

import Noe.preprocess as noe_preprocess
import Noe.make_viz as noe_make_viz
import Noe.hovertemplate as noe_hover

data = noe_preprocess.preprocess(match_infos, match_stats)

fig1 = noe_make_viz.create_scatter(data, noe_hover.get_scatter_hover_template())
fig2 = noe_make_viz.create_stacked_bars(data, noe_hover.get_stacked_bar_hover_template)

import Arman.preprocess as arman_preprocess
import Arman.make_viz as arman_makeviz

radar_data = arman_preprocess.preprocess(match_stats)
radar_fig = arman_makeviz.create_radar_chart(radar_data, 'Italy')

import khedrO.preprocess as khedro_preprocess
import khedrO.make_viz as khedro_make_viz

bubble_data = khedro_preprocess.preprocess_data(match_infos, player_stats, line_ups)

import Abdel.preprocess as abdel_preprocess
import Abdel.make_viz as abdel_makeviz

df1, df2 = abdel_preprocess.preprocess(player_stats, line_ups)
fig4, fig5 = abdel_makeviz.create_bars(df1, df2)

import Amadeus.preprocess as amadeus_preprocess
import Amadeus.make_viz as amadeus_makeviz

df1, df2, df3 = amadeus_preprocess.preprocess(player_stats, line_ups)
fig6, fig7, fig8 = amadeus_makeviz.draw(df1, df2, df3)

import Ibrahima.preprocess as ibrahima_preprocess
import Ibrahima.make_viz as ibrahima_makeviz

df = ibrahima_preprocess.preprocess(player_stats)
fig9 = ibrahima_makeviz.create_bar_chart(df)




app.layout = html.Div([
    html.Div(className='anchor', id='0'),
    html.Div(className='intro', children=[
        html.H1('SportsAI'),
        html.H2('Boost your Players with Data'),
    ]),
    html.Div(className='anchor', id='1'),
    html.Div(className='about_us', children=[
        html.Div(className='about-us-content', children=[
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
                html.Img(src='assets/img/aboutus.jpg', alt='A coach talking to her team'),
                html.A('Image Source',
                    href='https://www.nbcnews.com/news/world/italy-wins-european-soccer-championship-3-2-penalty-shootout-n1273643',
                    target='_blank')
            ])
        ])
    ]),
    html.Div(className='anchor', id='2'),
    html.Div(className='match-overview', children=[
        html.Div(className='match-overview-content', children=[
            html.Div(className='description', children=[
                html.H3('Match Overview'),
                html.P(
                    "The first group of visualizations includes multiple graphics that illustrate various aspects of the matches. " +
                    "These visualizations are designed to address general questions you might have and to introduce you to " +
                    "our work. Specifically, we present:"
                ),
                html.Ol(className='fig-description', children=[
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
            html.Div(className='viz-container', children=[
                html.Label('Select a plot:'),
                dcc.Dropdown(
                    id='type-dropdown',
                    options=[{'label': 'Total Score vs Fouls for Matches', 'value': 'scatter'},
                            {'label': 'Goals Scored in Open Play vs Set Pieces', 'value': 'horizontal_bar'}],
                    value='scatter',
                    clearable=False
                ),
                dcc.Graph(
                    figure=fig1,
                    className='graph',
                    id='scatter_horizontal_bar'
                )
            ])
        ])
    ]),
    html.Div(className='anchor', id='3'),
    html.Div(className='radar_chart', children=[
        html.Div(className='radar_chart_content', children=[
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
                    html.Li(
                        "Ball Possession % per Game: Average percentage of time the team has possession of the ball.")
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
                figure=radar_fig
            )
        ])
    ]),
    html.Div(className='anchor', id='4'),
    html.Div(className='weather_performance', children=[
        html.Div(className='weather_performance_content',children=[
            html.Div(className='description', children=[
                html.H3("Impact of Weather on Player Performance"),
                html.P(
                        "The bubble chart shows how meteorological conditions affect different players: "
                ),
                html.Ul([
                    html.Li("Each bubble represents the selected players performance for a match. The size of the bubble is proportional to the players' performance for the chosen statistic."),
                    html.Li("The color of the bubble indicates the average z-scores of temperature and humidity for the match in question."),
                    html.Li("Should there be no data for a particular player, for the chosen statistic, 'No data available.' will be displayed. For example, if you look at yellow cards, and the player has none"),
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
                    options=[{'label': stat, 'value': stat} for stat in player_stats['StatsName'].unique()]
                ),
                html.Div(id='output-container')
            ])
        ])
    ]),
    html.Div(className='anchor', id='5'),
    html.Div(className='peformance_metrics', children=[
        html.Div(className='performance-metrics-content', children=[
            html.Div(className='description',children=[
                html.H3('Performance Metrics'),
                html.P(
                    "This bar chart which provides a clear visual comparison of key performance metrics across different soccer player positions."+
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
                dcc.Graph(
                    figure=fig4,
                    className='graph',
                    id='bar1'
                )
            ])
        ])
    ]),
    html.Div(className='anchor', id='6'),
    html.Div(className='foot_analysis', children=[
        html.Div(className='foot-analysis-content', children=[
            html.Div(className='description', children=[
                html.H3('Foot Analysis'),
                html.P(
                    "This bar chart which provides a clear visualization of the number of goals scored by players in different positions "+
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
                dcc.Graph(
                    figure=fig5,
                    className='graph',
                    id='bar2'
                )
            ])
        ])
    ]),
    html.Div(className='anchor', id='7'),
    html.Div(className='stats_role', children=[
        html.Div(className='stats_role_content', children=[
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
    html.Div(className='anchor', id='8'),
    html.Div(className='tackles_bar', children=[
        html.Div(className='tackles_bar_content', children=[
            html.H3('Tackles'),
            html.P(
                "The following bar chart shows the number of tackles made by each player in the tournament. " +
                "Tackles are an important defensive metric that can help assess a player's ability to regain possession of the ball. " +
                "The chart provides insights into the defensive contributions of each player and highlights the top performers in this category."
            ),
            html.Div(className='viz-container', children=[
                dcc.Graph(
                    figure=fig9,
                    className='graph',
                    id='tackles-bar'
                )
            ])
        ]),
    ])
])

@app.callback(
    Output('scatter_horizontal_bar','figure'),
    Input('type-dropdown', 'value')
)
def update_graph(selected_type):
    if selected_type == 'scatter':
        return fig1
    if selected_type == 'horizontal_bar':
        return fig2
    
@app.callback(
    Output('radar1', 'figure'),
    Input('first-team-dropdown', 'value'),
    Input('second-team-dropdown', 'value')
)
def update_radar_chart(first_team, second_team):
    if first_team and second_team:
        radar_fig = arman_makeviz.create_radar_chart(radar_data, first_team)
        arman_makeviz.add_team_to_radar_chart(radar_fig, radar_data, second_team)
        return radar_fig
    if not first_team and not second_team:
        return arman_makeviz.create_empty_radar_chart()
    if not first_team:
        radar_fig = arman_makeviz.create_radar_chart(radar_data, second_team)
        return radar_fig
    if not second_team:
        radar_fig = arman_makeviz.create_radar_chart(radar_data, first_team)
        return radar_fig

@app.callback(
Output('player-dropdown', 'options'),
Input('country-dropdown', 'value')
)
def update_player_dropdown(selected_country):
    if selected_country:
        players = bubble_data[bubble_data['Country'] == selected_country]['FullName'].dropna().unique()
        return [{'label': player, 'value': player} for player in players]
    return []

@app.callback(
    Output('output-container', 'children'),
    [Input('country-dropdown', 'value'),
     Input('player-dropdown', 'value'),
     Input('stat-dropdown', 'value')]
)
def update_figure(selected_country, selected_player, selected_stat):
    filtered_df = bubble_data[bubble_data['Country'] == selected_country]
    filtered_df = filtered_df[filtered_df['FullName'] == selected_player]
    filtered_df = filtered_df[filtered_df['StatsName'] == selected_stat]


    if filtered_df.empty:
        return html.Div("Select a Country, Player and Statistic.", style={'color': 'red', 'font-size': '20px', 'text-align': 'center', 'margin-top': '20px'})
    if (filtered_df['Value'] == 0).all():
        return html.Div("No data available.", style={'color': 'red', 'font-size': '20px', 'text-align': 'center', 'margin-top': '20px'})

    return khedro_make_viz.create_figure(filtered_df)

@app.callback(
    Output('bar3', 'figure'),
    Input('plot-selector', 'value')
)
def update_graph(selected_plot):
    if selected_plot == 'contributions':
        return fig6
    elif selected_plot == 'goals':
        return fig7
    elif selected_plot == 'assists':
        return fig8

server = app.server