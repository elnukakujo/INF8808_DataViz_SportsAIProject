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

def draw(option,df):
    if option=="contributions":
        df=df.groupby("Role")["Total Contributions"].sum().sort_values(ascending=False)
        labels, values = prepare_bar_data(df)
        return create_bar_chart(labels, values, "Contributions by Role")
    elif option=="goals":
        df=df.groupby("Role")["Goals"].sum().sort_values(ascending=False)
        labels, values = prepare_bar_data(df)
        return create_bar_chart(labels, values, "Goals by Role")
    elif option=="assists":
        df=df.groupby("Role")["Assists"].sum().sort_values(ascending=False)
        labels, values = prepare_bar_data(df)
        return create_bar_chart(labels, values, "Assists by Role")