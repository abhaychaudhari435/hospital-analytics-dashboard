import streamlit as st

def show_cards(df):

    total = len(df)

    male = len(df[df["Gender"].astype(str).str.lower() == "male"])
    female = len(df[df["Gender"].astype(str).str.lower() == "female"])

    doctors = df["Doctor"].nunique()
    departments = df["Department"].nunique()
    diseases = df["Disease"].nunique()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "👥 Total Patients",
        total
    )

    c2.metric(
        "👨 Male",
        male
    )

    c3.metric(
        "👩 Female",
        female
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "👨‍⚕️ Doctors",
        doctors
    )

    c5.metric(
        "🏥 Departments",
        departments
    )

    c6.metric(
        "🦠 Diseases",
        diseases
    )