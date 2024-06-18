
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

app = dash.Dash(__name__)
app.title = 'SportsAI Project'

import get_df
match_infos = get_df.get_df('Match_information')
match_stats = get_df.get_df('Match_Stats')
player_stats = get_df.get_df('Players_stats')
line_ups= get_df.get_df('Line-ups')

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
fig3,fig4 = abdel_makeviz.create_bars(df1, df2)

import Amadeus.preprocess as amadeus_preprocess
import Amadeus.make_viz as amadeus_makeviz

df1, df2, df3 = amadeus_preprocess.preprocess(player_stats, line_ups)
fig5,fig6,fig7 = amadeus_makeviz.draw(df1, df2, df3)

app.layout = html.Div([
    html.Div(className='anchor',id='0'),
    html.Div(className='intro',children=[
        html.H2('SportsAI'),
        html.H1('Boost your Performance with Data'),
    ]),
    html.Div(className='anchor',id='1'),
    html.Div(className='about_us', children=[
        html.P(
            "At SportsAI, we are dedicated to revolutionizing the way coaches enhance their players' "+
            "performance through cutting-edge data visualization. Our team combines expertise in sports "+
            "science and advanced analytics to provide insightful, actionable data that empowers coaches to "+
            "make informed decisions. Whether it's tracking progress, identifying strengths and weaknesses, or "+ 
            "optimizing training strategies, SportsAI is your partner in achieving peak performance. Join us and "+
            "transform your data into a competitive edge."
        ),
        html.Div(className='img-container',children=[
            html.Img(src='assets/img/aboutus.jpg', alt='A coach talking to her team'),
            html.A('Image Source', href='https://www.dickssportinggoods.com/protips/sports-and-activities/soccer/soccer-coaching-tips-game-day-prep', target='_blank')
        ])
    ]),
    html.Div(className='match-overview', children=[
        html.H3('Match Overview'),
        html.Div(className='description', children=[
            html.P(
                "The first group of visualizations includes multiple graphics that illustrate various aspects of the matches. "+
                "These visualizations are designed to address general questions that users might have and to introduce them to "+
                "our project. Specifically, we present:"
            ),
            html.Ol(className='fig-description', children=[
                html.Li("The number of goals scored and fouls committed in each match, under the assumption that the entertainment "+
                        "value of a game is correlated with the number of goals."
                ),
                html.Li("A comparison between the number of goals scored in open play and those scored from set pieces.")
            ]),
            html.P(
                "These visualizations offer a comprehensive overview of key match statistics, enhancing the understanding "+
                "of the factors that contribute to the dynamics of the game."
            ),
            html.P("Try hovering hover the elements in the graph to get more details!")
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
                    id='stacked-bar'
                )
        ])
    ]),
    html.Div(className='anchor',id='2'),
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
    html.Div(className='anchor',id='3'),
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
    html.Div(className='anchor',id='4'),
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
    ])
])

server = app.server