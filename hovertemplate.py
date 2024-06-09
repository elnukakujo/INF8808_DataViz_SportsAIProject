'''
    Provides the template for the tooltips.
'''


def get_score_hover_template():

    return ('<b>Match Teams :</b> %{x}'+
            '<br><b>Round :</b> %{customdata[0]}</br>'+
            '<b>Total score of the match:</b> %{y}<extra></extra>')
    
def get_fools_hover_template():

    return ('<b>Match Teams :</b> %{x}'+
            '<br><b>Round :</b> %{customdata[0]}</br>'+
            '<b>Fools of the Home Team:</b> %{customdata[1][0]}'+
            '<br><b>Fools of the Away Team:</b> %{customdata[1][1]}</br><extra></extra>')