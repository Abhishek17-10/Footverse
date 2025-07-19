import streamlit as st
import pandas as pd
import plotly.express as px

def show_global_heatmap():
    st.title("🌍 Global Football Heatmaps")
    st.markdown("Visualize player distribution and average attributes by country using interactive maps.")

    # Load data
    try:
        df = pd.read_csv("fifa_players.csv")
    except FileNotFoundError:
        st.error("❌ File 'players.csv' not found.")
        return

    # Validate nationality column
    if 'nationality' not in df.columns:
        st.error("❌ Column 'nationality' not found in the dataset.")
        return

    # Player Count Heatmap
    st.subheader("1️⃣ Player Distribution by Country")
    player_counts = df['nationality'].value_counts().reset_index()
    player_counts.columns = ['Country', 'Player Count']

    fig1 = px.choropleth(
        player_counts,
        locations='Country',
        locationmode='country names',
        color='Player Count',
        color_continuous_scale='Turbo',
        hover_name='Country',
        title='🌍 Number of Players per Country',
    )
    fig1.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
    st.plotly_chart(fig1, use_container_width=True)

    # Stat dropdown for heatmap
    st.subheader("2️⃣ Average Attribute by Country")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    # Filter out irrelevant columns if needed
    exclude = ['age', 'height_cm', 'weight_kgs']
    stat_options = [col for col in numeric_cols if col not in exclude]

    selected_stat = st.selectbox("Choose an attribute to map:", stat_options, index=stat_options.index("overall_rating") if "overall_rating" in stat_options else 0)

    stat_map = df.groupby('nationality')[selected_stat].mean().reset_index()
    stat_map.columns = ['Country', 'Average Stat']

    fig2 = px.choropleth(
        stat_map,
        locations='Country',
        locationmode='country names',
        color='Average Stat',
        color_continuous_scale='Viridis',
        hover_name='Country',
        title=f'🔥 Average {selected_stat.replace("_", " ").title()} by Country',
    )
    fig2.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
    st.plotly_chart(fig2, use_container_width=True)



