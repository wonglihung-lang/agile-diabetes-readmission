
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(
    "/content/drive/MyDrive/Agile Data Science PMA/diabetic_data.csv"
)

# ==================================================
# TITLE
# ==================================================

st.title("Diabetes Readmission Prediction Dashboard")

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3 = st.columns(3)

readmission_rate = (
    (df["readmitted"] == "<30").mean()
) * 100

with col1:
    st.metric(
        "Total Patients",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Readmission Rate",
        f"{readmission_rate:.2f}%"
    )

with col3:
    st.metric(
        "Average Stay",
        f"{df['time_in_hospital'].mean():.1f} Days"
    )

# ==================================================
# SIDEBAR FILTERS
# ==================================================

st.sidebar.header("Filters")

gender = st.sidebar.selectbox(
    "Gender",
    sorted(df["gender"].unique())
)

age_group = st.sidebar.selectbox(
    "Age Group",
    sorted(df["age"].unique())
)

filtered_df = df[
    (df["gender"] == gender)
    &
    (df["age"] == age_group)
]

# ==================================================
# CHART 1
# ==================================================

st.subheader("Readmission Distribution")

fig, ax = plt.subplots()

filtered_df["readmitted"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# ==================================================
# CHART 2
# ==================================================

st.subheader("Age Group Distribution")

fig, ax = plt.subplots()

filtered_df["age"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# ==================================================
# CHART 3
# ==================================================

st.subheader("Time in Hospital Distribution")

fig, ax = plt.subplots()

ax.hist(
    filtered_df["time_in_hospital"],
    bins=14
)

st.pyplot(fig)

# ==================================================
# PREDICTION SECTION
# ==================================================

st.header("Readmission Risk Prediction")

age = st.number_input(
    "Age Group (0-9)",
    0,
    9,
    5
)

stay = st.number_input(
    "Time in Hospital",
    1,
    14,
    5
)

meds = st.number_input(
    "Number of Medications",
    0,
    100,
    10
)

if st.button("Predict"):

    if meds > 20 or stay > 7:
        st.error("High Readmission Risk")
    else:
        st.success("Low Readmission Risk")
