'''
    Provides the template for the tooltips.
'''

def get_scatter_hover_template():
    return ('<span style="font-family: Montserrat-Medium">Match:</span> %{customdata[1]}<br>'
            '<span style="font-family: Montserrat-Medium">Round:</span> %{customdata[0]}<br>'
            '<span style="font-family: Montserrat-Medium">Total Goals:</span> %{x}<br>'
            '<span style="font-family: Montserrat-Medium">Total Fouls:</span> %{y}<br><extra></extra>')

def get_stacked_bar_hover_template(mode):
    return ('<span style="font-family: Montserrat-Medium">Match Teams :</span> %{y}<br>'+
            '<span style="font-family: Montserrat-Medium">Round :</span> %{customdata}<br>'+
            f'<span style="font-family: Montserrat-Medium">{mode}:</span>'+' %{x}<extra></extra>')