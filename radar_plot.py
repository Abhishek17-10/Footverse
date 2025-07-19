import plotly.graph_objects as go

def create_radar_plot(categories, values1, values2, label1, label2):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values1,
        theta=categories,
        fill='toself',
        name=label1,
        line=dict(color='royalblue')
    ))

    fig.add_trace(go.Scatterpolar(
        r=values2,
        theta=categories,
        fill='toself',
        name=label2,
        line=dict(color='firebrick')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, max(max(values1), max(values2)) + 10])
        ),
        showlegend=True,
        title="🧠 Player Attribute Comparison"
    )

    return fig

