import streamlit as st
from utils.google_sheet import load_data
from dashboard.sidebar import sidebar
from dashboard.cards import show_cards
from dashboard.charts import show_charts

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="All Is Well Hospital Data - Sheet1.csv",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

.block-container{
padding-top:1rem;
padding-bottom:1rem;
padding-left:2rem;
padding-right:2rem;
}

h1{
color:#4FC3F7;
font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🏥 ALL IS WELL HOSPITAL ANALYTICS DASHBOARD")

st.caption("Real-Time Hospital Analytics using Google Sheets")

st.divider()

# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = load_data()

if df.empty:

    st.error("Google Sheet has no data.")

    st.stop()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

filters = sidebar(df)

filtered_df = df.copy()

# --------------------------------------------------
# Search
# --------------------------------------------------

if filters["search"] != "":

    filtered_df = filtered_df[
        filtered_df["Patient Name"]
        .astype(str)
        .str.contains(filters["search"],case=False)
    ]

# --------------------------------------------------
# Gender
# --------------------------------------------------

if filters["gender"] != "All":

    filtered_df = filtered_df[
        filtered_df["Gender"] == filters["gender"]
    ]

# --------------------------------------------------
# Disease
# --------------------------------------------------

if filters["disease"] != "All":

    filtered_df = filtered_df[
        filtered_df["Disease"] == filters["disease"]
    ]

# --------------------------------------------------
# Doctor
# --------------------------------------------------

if filters["doctor"] != "All":

    filtered_df = filtered_df[
        filtered_df["Doctor"] == filters["doctor"]
    ]

# --------------------------------------------------
# Department
# --------------------------------------------------

if filters["department"] != "All":

    filtered_df = filtered_df[
        filtered_df["Department"] == filters["department"]
    ]

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

show_cards(filtered_df)

st.markdown("<br>",unsafe_allow_html=True)

# --------------------------------------------------
# Charts
# --------------------------------------------------

show_charts(filtered_df)

st.divider()

# --------------------------------------------------
# Patient Table
# --------------------------------------------------

st.subheader("📋 Patient Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

st.success(f"Showing {len(filtered_df)} Patient(s)")

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
"""
<center>

Abhay chaudhari

</center>
""",
unsafe_allow_html=True
)