'''
    Provides the template for the tooltips.
'''

def get_scatter_hover_template()->str:
    '''
        Returns the template for the scatter plot showing the match name, round name, total goals and fouls.
        
        Returns:    
            The styled hovertemplate
    '''
    return ('<span style="font-family: Montserrat-Medium">Match:</span> <span style="font-family: Roboto-Light">%{customdata[1]}</span><br>'+
            '<span style="font-family: Montserrat-Medium">Round:</span> <span style="font-family: Roboto-Light">%{customdata[0]}</span><br>'+
            '<span style="font-family: Montserrat-Medium">Total Goals:</span> <span style="font-family: Roboto-Light">%{customdata[2]}</span><br>'+
            '<span style="font-family: Montserrat-Medium">Total Fouls:</span> <span style="font-family: Roboto-Light">%{y}</span><br><extra></extra>')

def get_stacked_bar_hover_template(mode: str)->str:
    '''
        Returns the template for the scatter plot showing the match teams, round name, the type of goal and value.
        
        Args:
            mode (str): The type of goal
        
        Returns:    
            The styled hovertemplate
    '''
    return ('<span style="font-family: Montserrat-Medium">Match Teams :</span> <span style="font-family: Roboto-Light">%{y}</span><br>'+
            '<span style="font-family: Montserrat-Medium">Round :</span> <span style="font-family: Roboto-Light">%{customdata}</span><br>'+
            f'<span style="font-family: Montserrat-Medium">{mode}:</span>'+' <span style="font-family: Roboto-Light">%{x}</span><extra></extra>')