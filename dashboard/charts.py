import streamlit as st
import plotly.express as px


def show_charts(df):

    c1,c2=st.columns(2)

    with c1:

        disease=df["Disease"].value_counts().reset_index()

        disease.columns=["Disease","Count"]

        fig=px.pie(
            disease,
            names="Disease",
            values="Count",
            hole=.45,
            title="Disease Distribution"
        )

        st.plotly_chart(fig,use_container_width=True)

    with c2:

        gender=df["Gender"].value_counts().reset_index()

        gender.columns=["Gender","Count"]

        fig=px.pie(
            gender,
            names="Gender",
            values="Count",
            hole=.45,
            title="Gender Distribution"
        )

        st.plotly_chart(fig,use_container_width=True)



    c3,c4=st.columns(2)

    with c3:

        doctor=df["Doctor"].value_counts().reset_index()

        doctor.columns=["Doctor","Patients"]

        fig=px.bar(
            doctor,
            x="Doctor",
            y="Patients",
            color="Patients",
            title="Doctor Wise Patients"
        )

        st.plotly_chart(fig,use_container_width=True)



    with c4:

        dept=df["Department"].value_counts().reset_index()

        dept.columns=["Department","Patients"]

        fig=px.bar(
            dept,
            x="Department",
            y="Patients",
            color="Patients",
            title="Department Wise Patients"
        )

        st.plotly_chart(fig,use_container_width=True)