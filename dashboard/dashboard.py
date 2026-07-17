import streamlit as st

def show_cards(df):

    total_patients = len(df)

    male_patients = len(df[df["Gender"].astype(str).str.lower()=="male"])
    female_patients = len(df[df["Gender"].astype(str).str.lower()=="female"])

    total_doctors = df["Doctor"].nunique()
    total_departments = df["Department"].nunique()
    total_diseases = df["Disease"].nunique()

    admitted = len(df[df["Status"].astype(str).str.lower()=="admitted"])
    discharged = len(df[df["Status"].astype(str).str.lower()=="discharged"])
    critical = len(df[df["Status"].astype(str).str.lower()=="critical"])

    rooms = df["Room No"].nunique()
    wards = df["Ward"].nunique()

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("👥 Patients", total_patients)
    c2.metric("👨 Male", male_patients)
    c3.metric("👩 Female", female_patients)
    c4.metric("👨‍⚕️ Doctors", total_doctors)
    c5.metric("🏥 Departments", total_departments)

    st.divider()

    c6,c7,c8,c9,c10 = st.columns(5)

    c6.metric("🦠 Diseases", total_diseases)
    c7.metric("🛏️ Rooms", rooms)
    c8.metric("🏨 Wards", wards)
    c9.metric("✅ Admitted", admitted)
    c10.metric("🏠 Discharged", discharged)

    if critical > 0:
        st.error(f"🚨 Critical Patients : {critical}")