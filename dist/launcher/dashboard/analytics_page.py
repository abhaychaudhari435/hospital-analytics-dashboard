import streamlit as st
import plotly.express as px

from utils.analytics_data import load_all_data

def analytics_page():

    st.title("📊 Hospital Analytics")

    patients, medical, revenue = load_all_data()

    if patients.empty or medical.empty or revenue.empty:
        st.error("Some data could not be loaded.")
        return

    total_patients = len(patients)
    total_medicines = len(medical)
    total_revenue = revenue["Amount"].sum()
    departments = patients["Department"].nunique()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("👥 Patients", total_patients)
    c2.metric("💊 Medicines", total_medicines)
    c3.metric("💰 Revenue", f"₹{total_revenue:,.0f}")
    c4.metric("🏥 Departments", departments)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        fig = px.pie(
            patients,
            names="Gender",
            title="Gender Distribution",
            hole=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.pie(
            patients,
            names="Disease",
            title="Disease Distribution",
            hole=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        dept = revenue.groupby("Department")["Amount"].sum().reset_index()

        fig = px.bar(
            dept,
            x="Department",
            y="Amount",
            color="Amount",
            title="Revenue by Department"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        top = medical.sort_values("Sold", ascending=False)

        fig = px.bar(
            top,
            x="Medicine Name",
            y="Sold",
            color="Category",
            title="Top Selling Medicines"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("🏆 Hospital Summary")

    left, right = st.columns(2)

    with left:

        st.success(
            f"🦠 Most Common Disease : {patients['Disease'].mode()[0]}"
        )

        st.success(
            f"💊 Top Medicine : {medical.sort_values('Sold',ascending=False).iloc[0]['Medicine Name']}"
        )

        st.success(
            f"👥 Average Age : {patients['Age'].mean():.1f}"
        )

    with right:

        st.success(
            f"💰 Total Bills : {len(revenue)}"
        )

        st.success(
            f"🏥 Best Department : {revenue.groupby('Department')['Amount'].sum().idxmax()}"
        )

        st.success(
            f"👨‍⚕ Top Doctor : {revenue.groupby('Doctor')['Amount'].sum().idxmax()}"
        )