import streamlit as st
import plotly.express as px
from utils.revenue_sheet import load_revenue_data


def revenue_page():

    st.title("💰 Revenue Dashboard")

    df = load_revenue_data()

    if df.empty:
        st.error("Revenue data not found.")
        return

    # -------------------------
    # KPIs
    # -------------------------

    total_revenue = df["Amount"].sum()
    total_bills = len(df)
    avg_bill = df["Amount"].mean()
    departments = df["Department"].nunique()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
    c2.metric("🧾 Total Bills", total_bills)
    c3.metric("📊 Avg Bill", f"₹{avg_bill:,.0f}")
    c4.metric("🏥 Departments", departments)

    st.divider()

    # -------------------------
    # Search
    # -------------------------

    search = st.text_input("🔍 Search Patient")

    if search:
        df = df[df["Patient Name"].str.contains(search, case=False)]

    # -------------------------
    # Charts
    # -------------------------

    left, right = st.columns(2)

    with left:

        payment = df["Payment Mode"].value_counts().reset_index()

        payment.columns = ["Payment Mode", "Count"]

        fig = px.pie(
            payment,
            names="Payment Mode",
            values="Count",
            hole=0.5,
            title="Payment Mode Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        dept = df.groupby("Department")["Amount"].sum().reset_index()

        fig = px.bar(
            dept,
            x="Department",
            y="Amount",
            color="Amount",
            title="Revenue by Department"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    left, right = st.columns(2)

    with left:

        doctor = df.groupby("Doctor")["Amount"].sum().reset_index()

        fig = px.bar(
            doctor,
            x="Doctor",
            y="Amount",
            color="Amount",
            title="Revenue by Doctor"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        daily = df.groupby("Date")["Amount"].sum().reset_index()

        fig = px.line(
            daily,
            x="Date",
            y="Amount",
            markers=True,
            title="Revenue Trend"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("🧾 Revenue Records")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )