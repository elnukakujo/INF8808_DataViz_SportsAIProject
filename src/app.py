
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

app = dash.Dash(__name__)
app.title = 'SportsAI Project'

import get_df

import Noe.preprocess as noe_preprocess
import Noe.make_viz as noe_make_viz
import plotly.io as pio
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

df1, df2 = abdel_preprocess.get_df(player_stats, line_ups)

fig3,fig4 = abdel_makeviz.create_bars(df1, df2)


app.layout = html.Div([
    html.H1('SportsAI Project'),
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
    ])
])
server = app.server