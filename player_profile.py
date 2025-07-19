import streamlit as st
import pandas as pd

def show_profile():
    st.title("🎯 Player Profile")

    # Load dataset
    df = pd.read_csv("fifa_players.csv")

    # Use 'name' instead of 'short_name'
    player_names = df['name'].dropna().unique()
    selected_player = st.selectbox("Select a player", sorted(player_names))

    player_data = df[df['name'] == selected_player].iloc[0]

    st.subheader(f"Profile: {selected_player}")
    st.write(f"**Full Name:** {player_data['full_name']}")
    st.write(f"**Age:** {player_data['age']}")
    st.write(f"**Nationality:** {player_data['nationality']}")
    st.write(f"**Height:** {player_data['height_cm']} cm")
    st.write(f"**Weight:** {player_data['weight_kgs']} kg")
    st.write(f"**Preferred Foot:** {player_data['preferred_foot']}")
    st.write(f"**Position(s):** {player_data['positions']}")
    st.write(f"**Overall Rating:** {player_data['overall_rating']}")
    st.write(f"**Potential:** {player_data['potential']}")
    st.write(f"**Value (€):** {player_data['value_euro']}")
    st.write(f"**Wage (€):** {player_data['wage_euro']}")
