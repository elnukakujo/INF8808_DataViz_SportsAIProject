import plotly.graph_objects as go


def create_radar_chart(merged_stats, team):
    team_stats = merged_stats[merged_stats['TeamName'] == team].iloc[0]

    categories = ['Goals Scored per Game',
                  'Attempts Accuracy',
                  'Passes Accuracy',
                  'Fouls Committed per Game',
                  'Ball Possession % per Game']

    values = [team_stats['Scaled Value Goals'],
              team_stats['Average Attempts % Accuracy'],
              team_stats['Average Passes Accuracy'],
              team_stats['Scaled Value Fouls'],  # Inverting fouls for better visualization
              team_stats['Average Ball Possession % per Game']]

    actual_values = [team_stats['Average Goals Scored per Game'],
                     team_stats['Average Attempts % Accuracy'],
                     team_stats['Average Passes Accuracy'],
                     team_stats['Average Fouls Committed per Game'],
                     team_stats['Average Ball Possession % per Game']]

    hover_template = (
        "<b>%{theta}</b><br>"
        "<b>Scaled Value: </b>%{r:.2f}<br>"
        "<b>Actual Value: </b>%{customdata:.2f}<extra></extra>"
    )

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=team,
        customdata=actual_values,
        hovertemplate=hover_template,
        line=dict(color='blue'),
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                showline=True,
                showgrid=True,
                gridcolor='gray',
                range=[0, 1]
            )),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        title=f'Team Comparison Radar Chart',
        hoverdistance=5
    )

    return fig

def add_team_to_radar_chart(fig, merged_stats, second_team):
    team_stats = merged_stats[merged_stats['TeamName'] == second_team].iloc[0]

    categories = ['Goals Scored per Game',
                  'Attempts Accuracy',
                  'Passes Accuracy',
                  'Fouls Committed per Game',
                  'Ball Possession % per Game']

    values = [team_stats['Scaled Value Goals'],
              team_stats['Average Attempts % Accuracy'],
              team_stats['Average Passes Accuracy'],
              team_stats['Scaled Value Fouls'],
              team_stats['Average Ball Possession % per Game']]

    actual_values = [team_stats['Average Goals Scored per Game'],
                     team_stats['Average Attempts % Accuracy'],
                     team_stats['Average Passes Accuracy'],
                     team_stats['Average Fouls Committed per Game'],
                     team_stats['Average Ball Possession % per Game']]

    hover_template = (
        "<b>%{theta}</b><br>"
        "<b>Scaled Value: </b> %{r:.2f}<br>"
        "<b>Actual Value: </b>%{customdata:.2f}<extra></extra>"
    )

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=second_team,
        customdata=actual_values,
        hovertemplate=hover_template,
        line=dict(color='red')
    ))

    return fig

def create_empty_radar_chart():
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                showline=True,
                showgrid=True,
                gridcolor='gray',
                range=[0, 1]
            )),
        title=f'Empty Radar Chart (Select a team)',
        hoverdistance=5,
        dragmode = False
    )
    return fig