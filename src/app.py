
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
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
app.title = 'SportsAI Project'

import Noe.template as template
import Noe.preprocess as preprocess
import Noe.make_viz as make_viz
import plotly.io as pio
import Noe.hovertemplate as hover

data = preprocess.preprocess()

pio.templates.default = 'simple_white'

fig1 = make_viz.create_scatter(data, hover.get_scatter_hover_template())
fig2 = make_viz.create_stacked_bars(data, hover.get_stacked_bar_hover_template)

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
    ])
])
server = app.server