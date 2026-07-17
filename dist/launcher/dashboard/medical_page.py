import streamlit as st
import plotly.express as px
from utils.medical_sheet import load_medical_data

def medical_page():

    st.title("💊 Medical Store Dashboard")

    df = load_medical_data()

    if df.empty:
        st.error("Medical data not found.")
        return

    total_medicines = len(df)
    total_stock = df["Stock"].sum()
    total_sold = df["Sold"].sum()
    total_value = (df["Stock"] * df["Unit Price"]).sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("💊 Medicines", total_medicines)
    c2.metric("📦 Stock", int(total_stock))
    c3.metric("✅ Sold", int(total_sold))
    c4.metric("💰 Inventory Value", f"₹{int(total_value):,}")

    st.divider()

    search = st.text_input("🔍 Search Medicine")

    if search:
        df = df[df["Medicine Name"].str.contains(search, case=False)]

    left, right = st.columns(2)

    with left:
        fig = px.pie(
            df,
            names="Category",
            title="Category Distribution",
            hole=0.5
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        top = df.sort_values("Sold", ascending=False)

        fig = px.bar(
            top,
            x="Medicine Name",
            y="Sold",
            color="Category",
            title="Top Selling Medicines"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("📋 Medicines")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )