# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: Noe Jager
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
'''

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

import Abdel.preprocess as abdel_preprocess
import Abdel.make_viz as abdel_makeviz

df1, df2 = abdel_preprocess.preprocess(player_stats, line_ups)
fig3, fig4 = abdel_makeviz.create_bars(df1, df2)

import Amadeus.preprocess as amadeus_preprocess
import Amadeus.make_viz as amadeus_makeviz

df1, df2, df3 = amadeus_preprocess.preprocess(player_stats, line_ups)
fig5, fig6, fig7 = amadeus_makeviz.draw(df1, df2, df3)

import Arman.preprocess as arman_preprocess
import Arman.make_viz as arman_makeviz

radar_data = arman_preprocess.preprocess(match_stats)
# fig8 = arman_makeviz.create_radar_chart(radar_data, 'Italy')

app.layout = html.Div([
    html.Div(className='anchor', id='0'),
    html.Div(className='intro', children=[
        html.H1('SportsAI'),
        html.H2('Boost your Players with Data'),
    ]),
    html.Div(className='anchor', id='1'),
    html.Div(className='about_us', children=[
        html.P(
            "At SportsAI, we are dedicated to revolutionizing the way coaches enhance their players' " +
            "performance through cutting-edge data visualization. Our team combines expertise in sports " +
            "science and advanced analytics to provide insightful, actionable data that empowers coaches to " +
            "make informed decisions. Whether it's tracking progress, identifying strengths and weaknesses, or " +
            "optimizing training strategies, SportsAI is your partner in achieving peak performance. Join us and " +
            "transform your data into a competitive edge."
        ),
        html.Div(className='img-container', children=[
            html.Img(src='assets/img/aboutus.jpg', alt='A coach talking to her team'),
            html.A('Image Source',
                   href='https://www.nbcnews.com/news/world/italy-wins-european-soccer-championship-3-2-penalty-shootout-n1273643',
                   target='_blank')
        ])
    ]),
    html.Div(className='match-overview', children=[
        html.H3('Match Overview'),
        html.Div(className='description', children=[
            html.P(
                "The first group of visualizations includes multiple graphics that illustrate various aspects of the matches. " +
                "These visualizations are designed to address general questions that users might have and to introduce them to " +
                "our project. Specifically, we present:"
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
            dcc.Graph(
                figure=fig1,
                config=dict(
                    scrollZoom=False,
                    showTips=False,
                    showAxisDragHandles=False,
                    doubleClick=False,
                    displayModeBar=False
                ),
                className='graph',
                id='scatter-plot'
            ),
            html.Tr(),
            dcc.Graph(
                figure=fig2,
                config=dict(
                    scrollZoom=False,
                    showTips=False,
                    showAxisDragHandles=False,
                    doubleClick=False,
                    displayModeBar=False
                ),
                className='graph',
                id='stacked-bar',
                style={"margin-left": "100px"}
            )
        ])
    ]),
    html.Div(className='anchor', id='2'),
    html.Div(className='viz-container', children=[
        dcc.Graph(
            figure=fig3,
            config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            ),
            className='graph',
            id='bar1'
        )
    ]),
    html.Div(className='anchor', id='3'),
    html.Div(className='viz-container', children=[
        dcc.Graph(
            figure=fig4,
            config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            ),
            className='graph',
            id='bar2'
        )
    ]),
    html.Div(className='anchor', id='4'),
    html.Div(id='pie-charts', children=[
        html.Div(className='viz-container', children=[
            dcc.Graph(
                figure=fig5,
                config=dict(
                    scrollZoom=False,
                    showTips=False,
                    showAxisDragHandles=False,
                    doubleClick=False,
                    displayModeBar=False
                ),
                className='graph',
                id='pie1'
            ),
        ]),
        html.Div(className='viz-container', children=[
            dcc.Graph(
                figure=fig6,
                config=dict(
                    scrollZoom=False,
                    showTips=False,
                    showAxisDragHandles=False,
                    doubleClick=False,
                    displayModeBar=False
                ),
                className='graph',
                id='pie2'
            ),
        ]),
        html.Div(className='viz-container', children=[
            dcc.Graph(
                figure=fig7,
                config=dict(
                    scrollZoom=False,
                    showTips=False,
                    showAxisDragHandles=False,
                    doubleClick=False,
                    displayModeBar=False
                ),
                className='graph',
                id='pie3'
            )
        ])
    ]),
    html.Div(className='anchor', id='5'),
    html.Div([
        html.Div(className='radar-chart-section', children=[
            html.Div(className='radar-chart-explanation', children=[
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
                ]),
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
                )
            ]),
            html.Div(className='radar-chart-container', children=[
                dcc.Graph(
                    id='radar-chart',
                    config=dict(
                        scrollZoom=True,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                    className='radar-chart'
                )
            ])
        ])
    ])
])

@app.callback(
    Output('radar-chart', 'figure'),
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


server = app.server
