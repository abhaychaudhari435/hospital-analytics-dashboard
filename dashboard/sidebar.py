import streamlit as st

def sidebar():

    st.sidebar.title("🏥 All Is Well Hospital")

    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "Navigation",
        [
            "🏥 Dashboard",
            "👥 Patients",
            "💊 Medical Store",
            "💰 Revenue",
            "📊 Analytics",
            "⚙️ Settings",
            "ℹ️ About"
        ]
    )

    st.sidebar.markdown("---")

    if st.sidebar.button("🔄 Refresh Dashboard", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

    st.sidebar.markdown("---")

    st.sidebar.caption("Hospital Analytics Dashboard v2.0")

    return page