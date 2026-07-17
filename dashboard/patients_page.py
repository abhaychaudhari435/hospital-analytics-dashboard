import streamlit as st
from utils.google_sheet import load_data

def patients_page():

    st.title("👥 Patients")

    # ---------------- Load Data ---------------- #

    df = load_data()

    # ---------------- Search ---------------- #

    search = st.text_input(
        "🔍 Search Patient (Name / Patient ID / Room / Doctor / Disease)"
    )

    if search:
        df = df[
            df.astype(str)
            .apply(lambda x: x.str.contains(search, case=False, na=False))
            .any(axis=1)
        ]

    # ---------------- Sidebar Filters ---------------- #

    room = st.sidebar.selectbox(
        "🏥 Room",
        ["All"] + sorted(df["Room No"].dropna().unique().tolist())
    )

    ward = st.sidebar.selectbox(
        "🏨 Ward",
        ["All"] + sorted(df["Ward"].dropna().unique().tolist())
    )

    status = st.sidebar.selectbox(
        "📋 Status",
        ["All"] + sorted(df["Status"].dropna().unique().tolist())
    )

    doctor = st.sidebar.selectbox(
        "👨‍⚕️ Doctor",
        ["All"] + sorted(df["Doctor"].dropna().unique().tolist())
    )

    department = st.sidebar.selectbox(
        "🏥 Department",
        ["All"] + sorted(df["Department"].dropna().unique().tolist())
    )

    disease = st.sidebar.selectbox(
        "🦠 Disease",
        ["All"] + sorted(df["Disease"].dropna().unique().tolist())
    )

    gender = st.sidebar.selectbox(
        "🚻 Gender",
        ["All"] + sorted(df["Gender"].dropna().unique().tolist())
    )

    # ---------------- Apply Filters ---------------- #

    if room != "All":
        df = df[df["Room No"] == room]

    if ward != "All":
        df = df[df["Ward"] == ward]

    if status != "All":
        df = df[df["Status"] == status]

    if doctor != "All":
        df = df[df["Doctor"] == doctor]

    if department != "All":
        df = df[df["Department"] == department]

    if disease != "All":
        df = df[df["Disease"] == disease]

    if gender != "All":
        df = df[df["Gender"] == gender]

    # ---------------- Metrics ---------------- #

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Total Patients", len(df))
    col2.metric("🏥 Rooms", df["Room No"].nunique())
    col3.metric("👨‍⚕️ Doctors", df["Doctor"].nunique())
    col4.metric("🏨 Wards", df["Ward"].nunique())

    st.divider()

    # ---------------- Patient Found ---------------- #

    if len(df) == 1:

        patient = df.iloc[0]

        st.success(
            f"""
### ✅ Patient Found

👤 **{patient['Patient Name']}**

🆔 Patient ID : **{patient['Patient ID']}**

🏥 Room : **{patient['Room No']}**

🏨 Ward : **{patient['Ward']}**

🛏️ Bed : **{patient['Bed No']}**

📋 Status : **{patient['Status']}**

👨‍⚕️ Doctor : **{patient['Doctor']}**

🩺 Disease : **{patient['Disease']}**

📍 Department : **{patient['Department']}**
"""
        )

    # ---------------- Download ---------------- #

    st.download_button(
        "⬇️ Download Patient Data",
        df.to_csv(index=False),
        "patients.csv",
        "text/csv"
    )

    st.divider()

    # ---------------- Table ---------------- #

    st.dataframe(
        df[
            [
                "Patient ID",
                "Patient Name",
                "Age",
                "Gender",
                "Phone",
                "Address",
                "Disease",
                "Department",
                "Doctor",
                "Room No",
                "Ward",
                "Bed No",
                "Status",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )