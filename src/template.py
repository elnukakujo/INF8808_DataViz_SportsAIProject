'''
    Creates the theme to be used in our bar chart.
'''
import plotly.graph_objects as go
import plotly.io as pio


def create_template():
    # TODO : Define a theme as defined above
    pio.templates['mytemplate'] = go.layout.Template(
        layout=go.Layout(
            title=dict(
                font_size=14,
                font_family='Montserrat-Medium'
            ),
            legend=dict(
                title=dict(
                    font=dict(
                        size=14,
                        family='Montserrat-Medium'
                    )
                ),
                font=dict(
                    size=11,
                    family='Roboto-Light'
                )
            ),
            xaxis=dict(
                titlefont=dict(
                    size=14,
                    family='Montserrat-Medium'
                ),
                tickfont=dict(
                    size=11,
                    family='Roboto-Light'
                )
            ),
            yaxis=dict( 
                titlefont=dict(
                    size=14,
                    family='Montserrat-Medium'
                ),
                tickfont=dict(
                    size=11,
                    family='Roboto-Light'
                )
            )
        )
    )