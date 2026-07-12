from utils.google_sheet import load_data
from utils.medical_sheet import load_medical_data
from utils.revenue_sheet import load_revenue_data

def load_all_data():

    patients = load_data()

    medical = load_medical_data()

    revenue = load_revenue_data()

    return patients, medical, revenue