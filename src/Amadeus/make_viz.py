import plotly.graph_objects as go

role_colors = {
    "forwards": "#636EFA",
    "midfielders": "#EF553B",
    "defenders": "#00CC96",
    "goalkeepers": "#AB63FA"
}

def prepare_bar_data(series):
    sorted_series = series.sort_values(ascending=True)
    labels = sorted_series.index
    values = sorted_series.values
    return labels, values

def create_bar_chart(labels, values, title):
    fig = go.Figure(data=[go.Bar(x=labels, y=values, marker=dict(color=[role_colors[label] for label in labels]))])
    fig.update_traces(
        hovertemplate='<b>%{x}</b><br>Total: %{y}<extra></extra>'
    )
    fig.update_layout(
        title_text=title,
        showlegend=False,
        xaxis_title="Player Position",
        yaxis_title="Counts",
    )
    return fig

def draw(df1, df2, df3):
    labels, values = prepare_bar_data(df1)
    fig_contributions = create_bar_chart(labels, values, "Contributions by Role")
    
    labels, values = prepare_bar_data(df2)
    fig_goals = create_bar_chart(labels, values, "Goals by Role")
    
    labels, values = prepare_bar_data(df3)
    fig_assists = create_bar_chart(labels, values, "Assists by Role")
    
    return fig_contributions, fig_goals, fig_assists
