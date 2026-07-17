import streamlit as st
from utils.google_sheet import load_data
from dashboard.cards import show_cards
from dashboard.charts import show_charts

def dashboard_page():

    st.title("🏥 Dashboard")

    st.caption("Real-Time Hospital Analytics Dashboard")

    df = load_data()

    if df.empty:
        st.error("No patient data found.")
        return

    show_cards(df)

    st.divider()

    show_charts(df)

    st.divider()

    st.subheader("📋 Recent Patients")

    st.dataframe(
        df.tail(10),
        use_container_width=True,
        hide_index=True
    )