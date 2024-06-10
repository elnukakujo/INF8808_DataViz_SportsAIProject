'''
    Provides the template for the tooltips.
'''


def get_bar_hover_template(mode):
    if mode=='TotalScore':
        return ('<b>Match Teams :</b> %{x}'+
                '<br><b>Round :</b> %{customdata[0]}</br>'+
                '<b>Total score of the match:</b> %{y}'+
                '<br><b>Scores of the Home Team:</b> %{customdata[1]}</br>'+
                '<b>Scores of the Away Team:</b> %{customdata[2]}<extra></extra>')
    elif mode=='TotalFouls':
        return ('<b>Match Teams :</b> %{x}'+
                '<br><b>Round :</b> %{customdata[0]}</br>'+
                '<b>Total fouls of the match:</b> %{y}'+
                '<br><b>Fouls of the Home Team:</b> %{customdata[1]}</br>'+
                '<b>Fouls of the Away Team:</b> %{customdata[2]}<extra></extra>')

def get_bubble_hover_template():
    return ('<b>Match Teams :</b> %{customdata[0]}'+
            '<br><b>Round :</b> %{customdata[1]}</br>'+
            '<b>Total score of the match:</b> %{x}'+
            '<br><b>Total fouls of the match:</b> %{y}<br><extra></extra>')

def get_stacked_bar_hover_template(mode):

    return (f'<b>Type of goal :</b> {mode}'+
            '<br><b>Match Teams :</b> %{x}</br>'+
            '<b>Round :</b> %{customdata}'+
            '<br><b>Goals:</b> %{y}</br><extra></extra>')