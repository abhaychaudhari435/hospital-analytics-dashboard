import streamlit as st
from datetime import datetime


def sidebar(df):
    with st.sidebar:

        st.markdown("## 🏥 ALL IS WELL")
        st.markdown("### Hospital Analytics")

        st.divider()

        st.markdown("### 📅 Date")
        st.info(datetime.now().strftime("%d %B %Y"))

        st.markdown("### ⏰ Time")
        st.info(datetime.now().strftime("%I:%M:%S %p"))

        st.divider()

        # -----------------------------
        # Search
        # -----------------------------

        search = st.text_input(
            "🔍 Search Patient",
            placeholder="Enter patient name..."
        )

        # -----------------------------
        # Gender Filter
        # -----------------------------

        gender = st.selectbox(
            "👤 Gender",
            ["All"] + sorted(df["Gender"].dropna().unique().tolist())
        )

        # -----------------------------
        # Disease Filter
        # -----------------------------

        disease = st.selectbox(
            "🦠 Disease",
            ["All"] + sorted(df["Disease"].dropna().unique().tolist())
        )

        # -----------------------------
        # Doctor Filter
        # -----------------------------

        doctor = st.selectbox(
            "👨‍⚕️ Doctor",
            ["All"] + sorted(df["Doctor"].dropna().unique().tolist())
        )

        # -----------------------------
        # Department Filter
        # -----------------------------

        department = st.selectbox(
            "🏥 Department",
            ["All"] + sorted(df["Department"].dropna().unique().tolist())
        )

        st.divider()

        refresh = st.button("🔄 Refresh Dashboard")

        return {
            "search": search,
            "gender": gender,
            "disease": disease,
            "doctor": doctor,
            "department": department,
            "refresh": refresh
        }