import pandas as pd

MEDICAL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTXujj_RQqU0A-96wUkfr5Ip0lyQVBdRyw_cWgcMU7hF-y-8lj1S5zCoDvoRuQEeUokzRPwMUoP0THl/pub?output=csv"

def load_medical_data():
    try:
        return pd.read_csv(MEDICAL_CSV)
    except:
        return pd.DataFrame()