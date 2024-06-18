import plotly.graph_objects as go

role_colors = {
    "forwards": "#636EFA",
    "midfielders": "#EF553B",
    "defenders": "#00CC96",
    "goalkeepers": "#AB63FA"
}

def prepare_pie_data(series):
    sorted_series = series.sort_values(ascending=True)
    total = sorted_series.sum()
    labels = sorted_series.index
    values = sorted_series.values
    return labels, values, total

def create_pie_chart(labels, values, title):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, sort=False)])
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        marker=dict(colors=[role_colors[label] for label in labels]),
        hovertemplate='<b>%{label}</b><br>Total: %{value}<br>Percentage: %{percent:.2f}%<extra></extra>'
    )
    fig.update_layout(
        title_text=title,
        margin=dict(t=50, b=50, l=50, r=50),
        height=600,
        width=600,
        showlegend=True,
    )
    return fig

def draw(df1,df2,df3):
    labels, values, total = prepare_pie_data(df1)
    fig_contributions = create_pie_chart(labels, values, "Contributions by Role")
    
    labels, values, total = prepare_pie_data(df2)
    fig_goals = create_pie_chart(labels, values, "Goals by Role")
    
    labels, values, total = prepare_pie_data(df3)
    fig_assists = create_pie_chart(labels, values, "Assists by Role")
    
    return fig_contributions,fig_goals,fig_assists
