# formation_builder.py

import streamlit as st
from PIL import Image
import os

# Set your local pitch image path
PITCH_IMAGE_PATH = "assets/pitch.png"

# Default player positions for 4-3-3 formation
DEFAULT_FORMATION = {
    "GK": (50, 95),
    "LB": (20, 75),
    "CB": (40, 80),
    "CB": (60, 80),
    "RB": (80, 75),
    "CM": (35, 55),
    "CM": (50, 50),
    "CAM": (65, 55),
    "LW": (20, 30),
    "ST": (50, 25),
    "RW": (80, 30),
}

def draw_pitch():
    if not os.path.exists(PITCH_IMAGE_PATH):
        st.error("Pitch image not found. Please place 'pitch.png' in the 'assets' folder.")
        return None
    return Image.open(PITCH_IMAGE_PATH)

def show_formation_builder():
    st.title("🧩 Formation Builder")

    pitch = draw_pitch()
    if pitch is None:
        return

    st.image(pitch, use_column_width=True, caption="Drag-drop functionality coming soon!")

    st.subheader("Enter Player Names for 4-3-3 Formation")
    
    with st.form("formation_form"):
        player_inputs = {}
        for pos in DEFAULT_FORMATION.keys():
            player_inputs[pos] = st.text_input(f"{pos} Name", key=pos)
        submitted = st.form_submit_button("Submit Lineup")

    if submitted:
        st.success("Your formation has been created!")
        st.markdown("### 📝 Lineup:")
        for pos, name in player_inputs.items():
            st.markdown(f"**{pos}:** {name if name else 'N/A'}")




