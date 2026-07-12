import streamlit as st


def sidebar():

    st.sidebar.title("🏥 All Is Well Hospital")

    page = st.sidebar.radio(

        "Navigation",

        [

            "🏥 Dashboard",

            "👥 Patients",

            "💊 Medical Store",

            "💰 Revenue",

            "📊 Analytics",

            "⚙ Settings",

            "ℹ About"

        ]

    )

    return page