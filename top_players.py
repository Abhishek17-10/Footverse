import streamlit as st
import pandas as pd

def show_top_players():
    st.title("🏅 Top Players")

    # Load your data
    try:
        df = pd.read_csv("fifa_players.csv")  # Change path if needed
    except FileNotFoundError:
        st.error("❌ players.csv not found.")
        return

    # Dropdown for selecting attribute to rank players
    st.subheader("📊 Select Attribute to View Top Players")
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    # Remove columns that don't make sense for ranking
    exclude_cols = ["age", "height_cm", "weight_kgs", "wage_euro"]
    rankable_cols = [col for col in numeric_columns if col not in exclude_cols]

    attribute = st.selectbox("Choose attribute", sorted(rankable_cols))

    # Show top 10 players based on selected attribute
    top_df = df[["full_name", "nationality", "positions", attribute]].sort_values(by=attribute, ascending=False).head(10)

    st.markdown(f"### 🔝 Top 10 Players by **{attribute.replace('_', ' ').title()}**")
    st.dataframe(top_df.reset_index(drop=True), use_container_width=True)

    st.caption("Data Source: players.csv")



