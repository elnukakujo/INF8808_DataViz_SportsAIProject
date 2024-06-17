'''
    Creates the theme to be used in our pie chart.
'''
import plotly.graph_objects as go
import plotly.io as pio

THEME = {
    'background_color': '#ebf2fa',
    'font_family': 'Montserrat',
    'font_color': '#898989',
    'title_font_size': 20,
    'title_font_color': '#333333',
    'label_font_size': 14,
    'label_font_color': '#ffffff'
}

def create_template():
    '''
        Adds a new layout template to pio's templates.

        The template sets the font color and
        font to the values defined above in
        the THEME dictionary.

        The plot background and paper background
        are the background color defined
        above in the THEME dictionary.

        Also, sets the hover label to have a
        font size as defined for the label in the THEME dictionary.
        The hover label's font color is the same
        as the theme's overall font color. The hover mode
        is set to 'closest'.

        Also sets the colors for the pie slices
        to those defined in the THEME dictionary.

    '''
    pio.templates['pietemplate'] = go.layout.Template(
        layout=go.Layout(
            font=dict(
                family=THEME['font_family'],
                color=THEME['font_color']
            ),
            paper_bgcolor=THEME['background_color'],
            plot_bgcolor=THEME['background_color'],
            title=dict(
                font=dict(
                    size=THEME['title_font_size'],
                    color=THEME['title_font_color']
                )
            ),
            hoverlabel=dict(
                font_size=THEME['label_font_size'],
                font_color=THEME['label_font_color']
            ),
        )
    )