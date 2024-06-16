import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_renderer
import preprocess
import make_viz
import plotly.io as pio
import hovertemplate as hover

# Create the Dash app
app = dash.Dash(__name__)
app.title = 'SportsAI Project'

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

# Generate static HTML for the layout
html_string = '''
<!DOCTYPE html>
<html>
<head>
    <title>SportsAI Project</title>
    <!-- Include any CSS files or styles here -->
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>
{content}
</body>
</html>
'''.format(content=app.layout)

# Save the static HTML
with open("index.html", "w") as file:
    file.write(html_string)