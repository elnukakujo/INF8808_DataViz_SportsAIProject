
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

import Noe.preprocess as noe_preprocess
import Noe.make_viz as noe_make_viz
import Noe.hovertemplate as noe_hover

match_infos = get_df.get_df('Match information')
match_stats = get_df.get_df('Match Stats')
player_stats=get_df.get_df('Players stats')
line_ups=get_df.get_df('Line-ups')

pio.templates.default = 'simple_white'

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
    html.Nav([
        html.Ul([
            html.Li(html.A('SportsAI', href='#0')),
            html.Li([
                'Visualizations',
                html.Ul([
                    html.Li(html.A('Scatter Plot', href='#1')),
                    html.Li(html.A('Stacked Bar', href='#2')),
                    html.Li(html.A('Bar 1', href='#3')),
                    html.Li(html.A('Bar 2', href='#4')),
                    html.Li(html.A('Pie Chart', href='#5')),
                ], className='dropdown-content')
            ], className='dropdown')
        ])
    ], className='navbar'),
    html.Div(className='intro',children=[
        html.H1('SportsAI'),
        html.H2('Boost your Performance with Data'),
    ]),
    html.Div(className='anchor',id='1'),
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
                )
    ]),
    html.Div(className='anchor',id='2'),
    html.Div(className='viz-container', children=[
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
    ]),
    html.Div(className='anchor',id='3'),
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
    html.Div(className='anchor',id='4'),
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
    html.Div(className='anchor',id='5'),
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