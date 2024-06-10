import template as template
import preprocess
import make_viz
import plotly.io as pio
import hovertemplate as hover

sheet_names=['Match information','Match Stats']
columns={'Match information':['MatchID','HomeTeamName','AwayTeamName', 'RoundName','ScoreHome','ScoreAway'],
         'Match Stats':['MatchID','StatsName', 'Value']}

'''template.create_template()
pio.templates.default = 'simple_white+mytemplate' '''

df = preprocess.preprocess(sheet_names, columns)
print(df.head())
#fig = make_viz.create_bar(df,'TotalScore', ['RoundName','TeamScore'], hover.get_bar_hover_template)
#fig = make_viz.create_bar(df,'TotalFouls', ['RoundName','FoulsCommitted'], hover.get_bar_hover_template)
#fig = make_viz.create_bubble(df,'TotalScore','TotalFouls', ['MatchName','RoundName'], hover.get_bubble_hover_template())
fig = make_viz.create_stacked_bars(df,['GoalsOpenPlay','GoalsSetPieces'], 'RoundName', hover.get_stacked_bar_hover_template)
fig.show()