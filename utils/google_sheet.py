import pandas as pd
import streamlit as st

# ------------------------------------------------------------------
# Google Sheet CSV Link
# ------------------------------------------------------------------

GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSbwXLLuz0OmXNho3gSCn0TN2WeBDHi4kBSsTPqf-2dAm6wZzX5OkJEuA2NBCLLcePwCs8D0y2jFJTJ/pub?gid=0&single=true&output=csv"


# ------------------------------------------------------------------
# Load Data
# ------------------------------------------------------------------

@st.cache_data(ttl=10)
def load_data():

    try:
        df = pd.read_csv(GOOGLE_SHEET_URL)

        # Remove empty rows
        df.dropna(how="all", inplace=True)

        # Remove extra spaces from column names
        df.columns = df.columns.str.strip()

        # Convert Bill Amount to number
        if "Bill Amount" in df.columns:
            df["Bill Amount"] = pd.to_numeric(
                df["Bill Amount"],
                errors="coerce"
            ).fillna(0)

        # Convert Age to number
        if "Age" in df.columns:
            df["Age"] = pd.to_numeric(
                df["Age"],
                errors="coerce"
            ).fillna(0)

        return df

    except Exception as e:

        st.error("Unable to load Google Sheet")

        st.exception(e)

        return pd.DataFrame()