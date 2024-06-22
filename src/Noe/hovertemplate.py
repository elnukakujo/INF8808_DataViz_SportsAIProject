'''
    Provides the template for the tooltips.
'''

def get_scatter_hover_template():
    return ('<span style="font-family: Montserrat-Medium">Match:</span> <span style="font-family: Roboto-Light">%{customdata[1]}</span><br>'
            '<span style="font-family: Montserrat-Medium">Round:</span> <span style="font-family: Roboto-Light">%{customdata[0]}</span><br>'
            '<span style="font-family: Montserrat-Medium">Total Goals:</span> <span style="font-family: Roboto-Light">%{x}</span><br>'
            '<span style="font-family: Montserrat-Medium">Total Fouls:</span> <span style="font-family: Roboto-Light">%{y}</span><br><extra></extra>')

def get_stacked_bar_hover_template(mode):
    return ('<span style="font-family: Montserrat-Medium">Match Teams :</span> <span style="font-family: Roboto-Light">%{y}</span><br>'+
            '<span style="font-family: Montserrat-Medium">Round :</span> <span style="font-family: Roboto-Light">%{customdata}</span><br>'+
            f'<span style="font-family: Montserrat-Medium">{mode}:</span>'+' <span style="font-family: Roboto-Light">%{x}</span><extra></extra>')