import streamlit as st
from streamlit_option_menu import option_menu

# --- Page Config ---
st.set_page_config(page_title="Footverse", page_icon="⚽", layout="wide")

# --- Sidebar Navigation ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>⚽ Footverse</h2>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Home",
            "Player Comparison",
            "Player Attributes",
            "Top Players",
            "Global Heatmap 🌍",
            "Formation Builder 🧩",
            "Scout Reports 📋",
            "Team Stats 📊",
        ],
        icons=[
            "house",
            "people",
            "person",
            "trophy",
            "globe",
            "puzzle",
            "clipboard-data",
            "bar-chart",
        ],
        default_index=0,
    )

# --- Page Routing ---
if selected == "Home":
    col1, col2 = st.columns([1, 1])

    with col1:
        st.title("🏟️ Welcome to Footverse")
        st.markdown("""
        Explore the world of football like never before!  
        Track and compare players, scout rising stars,  
        and visualize key performance metrics with ease.

        ### 🚀 Key Features:
        - 📊 **Player Comparison** — Radar charts for visual analysis  
        - 🎯 **Player Attributes** — Explore detailed player stats  
        - 🏆 **Top Players** — Best performers by position  
        - 🌍 **Global Heatmap** — See country-wise talent spread  
        - 🧩 **Formation Builder** — Interactive drag-drop lineup  
        - 📋 *Scout Reports* — Coming soon  
        - 📊 *Team Stats* — Coming soon  

        👉 Use the **sidebar** to get started!
        """)

    with col2:
        st.image("https://miro.medium.com/v2/resize:fit:828/format:webp/1*qTPzLyKQZ3Hd6Mn7BdE2Pw.gif", width=400)

elif selected == "Player Comparison":
    from compare_players import compare_players
    compare_players()

elif selected == "Player Attributes":
    from player_attributes import show_player_attributes
    show_player_attributes()

elif selected == "Top Players":
    from top_players import show_top_players
    show_top_players()

elif selected == "Global Heatmap 🌍":
    from global_heatmap import show_global_heatmap
    show_global_heatmap()

elif selected == "Formation Builder 🧩":
    from formation_builder import show_formation_builder
    show_formation_builder()

elif selected == "Scout Reports 📋":
    st.title("📋 Scout Reports")
    st.info("Coming soon! Stay tuned for in-depth scouting reports.")

elif selected == "Team Stats 📊":
    st.title("📊 Team Stats")
    st.info("Coming soon! We'll help you analyze full team performances.")














