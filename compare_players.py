import streamlit as st
import pandas as pd
from radar_plot import create_radar_plot

def compare_players():
    st.title("⚔️ Compare Players")

    # Load dataset
    df = pd.read_csv("fifa_players.csv")
    df.columns = df.columns.str.lower()  # Standardize column names to lowercase

    # Drop duplicates just in case
    df = df.drop_duplicates(subset=['name'])

    # Select players
    player_names = df['name'].dropna().unique()
    player1 = st.selectbox("Player 1", player_names)
    player2 = st.selectbox("Player 2", player_names, index=1 if len(player_names) > 1 else 0)

    # Ensure different players
    if player1 == player2:
        st.warning("Please select two different players.")
        return

    # Define attributes to compare
    selected_attributes = [
        'acceleration', 'sprint_speed', 'finishing', 'short_passing',
        'vision', 'strength', 'shot_power', 'stamina', 'dribbling', 'ball_control'
    ]

    # Extract data for selected players
    player1_data = df[df['name'] == player1].iloc[0]
    player2_data = df[df['name'] == player2].iloc[0]

    # Prepare values for radar
    values1 = [player1_data[attr] for attr in selected_attributes]
    values2 = [player2_data[attr] for attr in selected_attributes]

    # Generate radar plot
    fig = create_radar_plot(selected_attributes, values1, values2, player1, player2)
    st.plotly_chart(fig, use_container_width=True)



