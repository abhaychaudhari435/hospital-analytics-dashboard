import pandas as pd
import streamlit as st

REVENUE_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSUFMO18z1mqNgMSyyMkxFkOvS6TbAHHoT2N_cOCURSDV81oDYBZKgglKOV1BmNxigcyecVcM3bjy_-/pub?output=csv"

@st.cache_data(ttl=60)
def load_revenue_data():
    try:
        df = pd.read_csv(REVENUE_CSV)

        # Remove empty rows
        df = df.dropna(how="all")

        # Remove extra spaces from column names
        df.columns = df.columns.str.strip()

        # Convert Amount to numeric
        if "Amount" in df.columns:
            df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)

        return df

    except Exception as e:
        st.error(f"Error loading Revenue Sheet: {e}")
        return pd.DataFrame()