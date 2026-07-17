import streamlit as st

def show_cards(df):
    total_patients = len(df)

    male_patients = len(df[df["Gender"].astype(str).str.lower() == "male"])
    female_patients = len(df[df["Gender"].astype(str).str.lower() == "female"])

    total_doctors = df["Doctor"].nunique()
    total_departments = df["Department"].nunique()
    total_diseases = df["Disease"].nunique()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👥 Total Patients", total_patients)

    with col2:
        st.metric("👨 Male Patients", male_patients)

    with col3:
        st.metric("👩 Female Patients", female_patients)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("👨‍⚕️ Doctors", total_doctors)

    with col5:
        st.metric("🏥 Departments", total_departments)

    with col6:
        st.metric("🦠 Diseases", total_diseases)