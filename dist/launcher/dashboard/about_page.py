import streamlit as st

def about_page():

    st.title("ℹ️ About")

    st.header("🏥 All Is Well Hospital Analytics Dashboard")

    st.write("""
This project is a Hospital Analytics Dashboard developed using Python,
Streamlit and Google Sheets.

The dashboard provides real-time hospital insights including:

• Patient Analytics

• Medical Store Analytics

• Revenue Analytics

• Interactive Charts

• Google Sheets Integration

• Live Dashboard

""")

    st.divider()

    st.subheader("🛠 Technologies Used")

    st.write("• Python")
    st.write("• Streamlit")
    st.write("• Plotly")
    st.write("• Pandas")
    st.write("• Google Sheets")

    st.divider()

    st.subheader("👨‍💻 Developed By")

    st.success("Abhay Chaudhari")

    st.write("School Project")

    st.write("2026")

    st.divider()

    st.info("Version : 2.0")