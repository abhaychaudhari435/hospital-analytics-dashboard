import streamlit as st

def settings_page():

    st.title("⚙️ Settings")

    st.subheader("Dashboard Preferences")

    theme = st.selectbox(
        "Theme",
        ["Light", "Dark"]
    )

    refresh = st.slider(
        "Auto Refresh (Seconds)",
        5,
        60,
        30
    )

    chart = st.selectbox(
        "Default Chart Style",
        [
            "Plotly",
            "Bar",
            "Pie",
            "Line"
        ]
    )

    st.divider()

    st.subheader("System Information")

    st.info("Hospital Analytics Dashboard v2.0")

    st.success("Google Sheets Connection : Connected ✅")

    st.success("Application Status : Running")

    st.write("Selected Theme :", theme)
    st.write("Refresh Time :", refresh, "Seconds")
    st.write("Chart Style :", chart)

    st.divider()

    st.button("Save Settings")