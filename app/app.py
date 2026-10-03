import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Hospital Readmission Prediction",
    page_icon="🏥",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "final_xgboost_model.pkl"
)

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #f5f7fa;
        margin-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🏥 Hospital Readmission Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict the likelihood of a patient being readmitted within 30 days.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PATIENT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">👤 Patient Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    race = st.selectbox(
        "Race",
        [
            "Caucasian",
            "AfricanAmerican",
            "Asian",
            "Hispanic",
            "Other",
            "Unknown"
        ]
    )

with col2:
    gender = st.selectbox(
        "Gender",
        [
            "Female",
            "Male"
        ]
    )

with col3:
    age = st.selectbox(
        "Age Group",
        [
            "[0-10)",
            "[10-20)",
            "[20-30)",
            "[30-40)",
            "[40-50)",
            "[50-60)",
            "[60-70)",
            "[70-80)",
            "[80-90)",
            "[90-100)"
        ]
    )


# ============================================================
# HOSPITAL INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🏥 Hospital Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    admission_type_id = st.number_input(
        "Admission Type ID",
        min_value=1,
        max_value=8,
        value=1,
        step=1
    )

with col2:
    discharge_disposition_id = st.number_input(
        "Discharge Disposition ID",
        min_value=1,
        max_value=30,
        value=1,
        step=1
    )

with col3:
    admission_source_id = st.number_input(
        "Admission Source ID",
        min_value=1,
        max_value=25,
        value=1,
        step=1
    )


# ============================================================
# HOSPITAL STAY INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🛏️ Hospital Stay Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    time_in_hospital = st.number_input(
        "Time in Hospital (days)",
        min_value=1,
        max_value=14,
        value=3,
        step=1
    )

with col2:
    num_lab_procedures = st.number_input(
        "Number of Lab Procedures",
        min_value=0,
        max_value=150,
        value=40,
        step=1
    )

with col3:
    num_procedures = st.number_input(
        "Number of Procedures",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

col1, col2, col3 = st.columns(3)

with col1:
    num_medications = st.number_input(
        "Number of Medications",
        min_value=0,
        max_value=100,
        value=15,
        step=1
    )

with col2:
    number_diagnoses = st.number_input(
        "Number of Diagnoses",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )

with col3:
    number_inpatient = st.number_input(
        "Previous Inpatient Visits",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )

col1, col2 = st.columns(2)

with col1:
    number_outpatient = st.number_input(
        "Previous Outpatient Visits",
        min_value=0,
        max_value=40,
        value=0,
        step=1
    )

with col2:
    number_emergency = st.number_input(
        "Previous Emergency Visits",
        min_value=0,
        max_value=80,
        value=0,
        step=1
    )


# ============================================================
# DIAGNOSIS INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🩺 Diagnosis Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    diag_1 = st.text_input(
        "Primary Diagnosis (diag_1)",
        value="250.00"
    )

with col2:
    diag_2 = st.text_input(
        "Secondary Diagnosis (diag_2)",
        value="250.00"
    )

with col3:
    diag_3 = st.text_input(
        "Additional Diagnosis (diag_3)",
        value="250.00"
    )


# ============================================================
# MEDICATION INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">💊 Medication Information</div>',
    unsafe_allow_html=True
)

medication_options = [
    "No",
    "Steady",
    "Up",
    "Down"
]

col1, col2, col3 = st.columns(3)

with col1:
    metformin = st.selectbox("Metformin", medication_options)

with col2:
    repaglinide = st.selectbox("Repaglinide", medication_options)

with col3:
    nateglinide = st.selectbox("Nateglinide", medication_options)

col1, col2, col3 = st.columns(3)

with col1:
    chlorpropamide = st.selectbox("Chlorpropamide", medication_options)

with col2:
    glimepiride = st.selectbox("Glimepiride", medication_options)

with col3:
    acetohexamide = st.selectbox("Acetohexamide", medication_options)

col1, col2, col3 = st.columns(3)

with col1:
    glipizide = st.selectbox("Glipizide", medication_options)

with col2:
    glyburide = st.selectbox("Glyburide", medication_options)

with col3:
    tolbutamide = st.selectbox("Tolbutamide", medication_options)

col1, col2, col3 = st.columns(3)

with col1:
    pioglitazone = st.selectbox("Pioglitazone", medication_options)

with col2:
    rosiglitazone = st.selectbox("Rosiglitazone", medication_options)

with col3:
    acarbose = st.selectbox("Acarbose", medication_options)

col1, col2, col3 = st.columns(3)

with col1:
    miglitol = st.selectbox("Miglitol", medication_options)

with col2:
    troglitazone = st.selectbox("Troglitazone", medication_options)

with col3:
    tolazamide = st.selectbox("Tolazamide", medication_options)

col1, col2, col3 = st.columns(3)

with col1:
    insulin = st.selectbox("Insulin", medication_options)

with col2:
    glyburide_metformin = st.selectbox(
        "Glyburide-Metformin",
        medication_options
    )

with col3:
    glipizide_metformin = st.selectbox(
        "Glipizide-Metformin",
        medication_options
    )

col1, col2, col3 = st.columns(3)

with col1:
    glimepiride_pioglitazone = st.selectbox(
        "Glimepiride-Pioglitazone",
        medication_options
    )

with col2:
    metformin_rosiglitazone = st.selectbox(
        "Metformin-Rosiglitazone",
        medication_options
    )

with col3:
    metformin_pioglitazone = st.selectbox(
        "Metformin-Pioglitazone",
        medication_options
    )


# ============================================================
# DIABETES INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🧪 Diabetes Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    change = st.selectbox(
        "Medication Change",
        [
            "No",
            "Ch"
        ]
    )

with col2:
    diabetesMed = st.selectbox(
        "Diabetes Medication Prescribed",
        [
            "Yes",
            "No"
        ]
    )


# ============================================================
# CREATE INPUT DATAFRAME
# ============================================================

input_data = pd.DataFrame({
    "admission_type_id": [admission_type_id],
    "discharge_disposition_id": [discharge_disposition_id],
    "admission_source_id": [admission_source_id],
    "time_in_hospital": [time_in_hospital],
    "num_lab_procedures": [num_lab_procedures],
    "num_procedures": [num_procedures],
    "num_medications": [num_medications],
    "number_outpatient": [number_outpatient],
    "number_emergency": [number_emergency],
    "number_inpatient": [number_inpatient],
    "number_diagnoses": [number_diagnoses],
    "race": [race],
    "gender": [gender],
    "age": [age],
    "diag_1": [diag_1],
    "diag_2": [diag_2],
    "diag_3": [diag_3],
    "metformin": [metformin],
    "repaglinide": [repaglinide],
    "nateglinide": [nateglinide],
    "chlorpropamide": [chlorpropamide],
    "glimepiride": [glimepiride],
    "acetohexamide": [acetohexamide],
    "glipizide": [glipizide],
    "glyburide": [glyburide],
    "tolbutamide": [tolbutamide],
    "pioglitazone": [pioglitazone],
    "rosiglitazone": [rosiglitazone],
    "acarbose": [acarbose],
    "miglitol": [miglitol],
    "troglitazone": [troglitazone],
    "tolazamide": [tolazamide],
    "insulin": [insulin],
    "glyburide-metformin": [glyburide_metformin],
    "glipizide-metformin": [glipizide_metformin],
    "glimepiride-pioglitazone": [glimepiride_pioglitazone],
    "metformin-rosiglitazone": [metformin_rosiglitazone],
    "metformin-pioglitazone": [metformin_pioglitazone],
    "change": [change],
    "diabetesMed": [diabetesMed]
})


# ============================================================
# PREDICTION
# ============================================================

st.markdown("---")

if st.button(
    "🔍 Predict 30-Day Readmission",
    use_container_width=True
):

    try:

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        st.markdown(
            '<div class="result-box">',
            unsafe_allow_html=True
        )

        if prediction == 1:

            st.error(
                "⚠️ Prediction: 30-Day Readmission"
            )

            st.metric(
                "Readmission Probability",
                f"{probability:.2%}"
            )

            st.warning(
                "The model predicts a higher likelihood of "
                "30-day readmission."
            )

        else:

            st.success(
                "✅ Prediction: No 30-Day Readmission"
            )

            st.metric(
                "Readmission Probability",
                f"{probability:.2%}"
            )

            st.info(
                "The model predicts a lower likelihood of "
                "30-day readmission."
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Hospital Readmission Prediction | "
    "Machine Learning Project using XGBoost"
)
