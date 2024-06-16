'''
    Provides the template for the tooltips.
'''

def get_scatter_hover_template():
    return ('<b>Match:</b> %{customdata[1]}<br>'
            '<b>Round:</b> %{customdata[0]}<br>'
            '<b>Total Goals:</b> %{x}<br>'
            '<b>Total Fouls:</b> %{y}<br><extra></extra>')

def get_stacked_bar_hover_template(mode):
    return ('<b>Match Teams :</b> %{y}<br>'+
            '<b>Round :</b> %{customdata}<br>'+
            f'<b>{mode}:</b>'+' %{x}<extra></extra>')