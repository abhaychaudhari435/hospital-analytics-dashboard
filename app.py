import streamlit as st

# ----------------------------
# Import Pages
# ----------------------------
from dashboard.sidebar import sidebar

from dashboard.dashboard_page import dashboard_page
from dashboard.patients_page import patients_page
from dashboard.medical_page import medical_page
from dashboard.revenue_page import revenue_page
from dashboard.analytics_page import analytics_page
from dashboard.settings_page import settings_page
from dashboard.about_page import about_page

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="All Is Well Hospital Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Sidebar
# ----------------------------
page = sidebar()

# ----------------------------
# Navigation
# ----------------------------
if page == "🏥 Dashboard":
    dashboard_page()

elif page == "👥 Patients":
    patients_page()

elif page == "💊 Medical Store":
    medical_page()

elif page == "💰 Revenue":
    revenue_page()

elif page == "📊 Analytics":
    analytics_page()

elif page == "⚙️ Settings":
    settings_page()

elif page == "ℹ️ About":
    about_page()

else:
    st.error("Page not found.")