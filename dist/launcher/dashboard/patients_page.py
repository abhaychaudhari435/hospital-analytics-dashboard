import streamlit as st
from utils.google_sheet import load_data

def patients_page():

    st.title("👥 Patients")

    df = load_data()

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )