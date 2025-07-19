import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load data
df = pd.read_csv("fifa_players.csv")
df.columns = df.columns.str.lower()

# Attribute groups
technical = ['crossing', 'finishing', 'short_passing', 'volleys', 'dribbling',
             'curve', 'freekick_accuracy', 'long_passing', 'ball_control']
physical = ['acceleration', 'sprint_speed', 'agility', 'reactions', 'balance',
            'shot_power', 'jumping', 'stamina', 'strength']
mental = ['vision', 'composure', 'positioning', 'interceptions', 'aggression']

all_attributes = technical + physical + mental

def draw_radar(player_data, player_name):
    values = [player_data.get(attr, 0) for attr in all_attributes]
    values += values[:1]
    labels = all_attributes + [all_attributes[0]]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        name=player_name,
        line=dict(color='royalblue', width=2)
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100]),
        ),
        showlegend=False,
        title=f"Radar Chart: {player_name}",
        title_font_size=20
    )

    st.plotly_chart(fig, use_container_width=True)

def show_strengths_and_weaknesses(player_data):
    st.subheader("🔍 Top Strengths & Weaknesses")
    attributes = {attr: player_data.get(attr, 0) for attr in all_attributes}
    sorted_attrs = sorted(attributes.items(), key=lambda x: x[1], reverse=True)

    top_3 = sorted_attrs[:3]
    bottom_3 = sorted_attrs[-3:]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 💪 Top 3 Strengths")
        for attr, val in top_3:
            st.markdown(f"✅ **{attr.replace('_', ' ').title()}**: {val}")

    with col2:
        st.markdown("### ⚠️ Bottom 3 Weaknesses")
        for attr, val in bottom_3:
            st.markdown(f"❌ **{attr.replace('_', ' ').title()}**: {val}")

def show_player_attributes():
    st.title("🎯 Player Attributes")

    # ✅ Add position filter
    unique_positions = sorted(df['positions'].dropna().unique())
    selected_position = st.selectbox("Filter by Position", ["All"] + unique_positions)

    if selected_position == "All":
        filtered_df = df
    else:
        filtered_df = df[df['positions'] == selected_position]

    player_name = st.selectbox("Select a Player", sorted(filtered_df['name'].dropna().unique()))

    player_data = filtered_df[filtered_df['name'] == player_name].iloc[0]

    st.subheader("🌐 Radar Chart")
    draw_radar(player_data, player_name)

    st.subheader("📊 Attribute Bar Chart")

    bar_data = pd.DataFrame({
        'Attribute': all_attributes,
        'Value': [player_data.get(attr, 0) for attr in all_attributes]
    })

    fig = go.Figure(go.Bar(
        x=bar_data['Attribute'],
        y=bar_data['Value'],
        marker_color='indigo'
    ))

    fig.update_layout(
        xaxis_tickangle=-45,
        title=f"{player_name} - Attribute Breakdown",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    show_strengths_and_weaknesses(player_data)

if __name__ == "__main__":
    show_player_attributes()


