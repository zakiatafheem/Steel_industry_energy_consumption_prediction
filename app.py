import streamlit as st
import pickle
import pandas as pd
import numpy as np

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("best_model.pkl", "rb"))

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Energy Predictor", layout="centered")

# -----------------------------
# CSS Styling
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f8;
    }

    h1 {
        text-align: center;
        color: #1f2937;
        font-weight: 700;
    }

    .section-title {
        font-size: 20px;
        font-weight: 600;
        margin-top: 20px;
        color: #374151;
    }

    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-size: 16px;
        font-weight: 600;
        border-radius: 10px;
        height: 3em;
        border: none;
    }

    .result-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #e8f5e9;
        text-align: center;
        font-size: 18px;
        margin-top: 15px;
    }

    .low-box {
        background-color: #e6f4ea;
        color: #166534;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
    }

    .high-box {
        background-color: #fdecea;
        color: #991b1b;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
    }

    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("Steel Energy Consumption Predictor")

st.caption("Estimate industrial energy usage based on operational parameters.")

# -----------------------------
# Input Section
# -----------------------------
st.markdown('<div class="section-title">🔧 Input Parameters</div>', unsafe_allow_html=True)

lagging_reactive = st.number_input("Lagging Reactive Power (kVarh)", 0.0)
leading_reactive = st.number_input("Leading Reactive Power (kVarh)", 0.0)

lagging_pf = st.number_input("Lagging Power Factor", 0.0)
leading_pf = st.number_input("Leading Power Factor", 0.0)

week_status = st.selectbox("Week Status", ["Weekday", "Weekend"])
day_of_week = st.selectbox("Day of Week",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

hour = st.slider("Hour of Day", 0, 23, 12)
day = st.slider("Day of Month", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)

# -----------------------------
# Feature Engineering
# -----------------------------
NSM = hour * 3600

NSM_sin = np.sin(2 * np.pi * NSM / 86400)
NSM_cos = np.cos(2 * np.pi * NSM / 86400)

month_sin = np.sin(2 * np.pi * month / 12)
month_cos = np.cos(2 * np.pi * month / 12)

# -----------------------------
# Centered Button
# -----------------------------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    predict = st.button("Predict")

# -----------------------------
# Prediction Section
# -----------------------------
if predict:

    st.markdown('<div class="section-title">📊 Prediction Result</div>', unsafe_allow_html=True)

    input_df = pd.DataFrame([{
        "Lagging_Current_Reactive_Power_kVarh": lagging_reactive,
        "Leading_Current_Reactive_Power_kVarh": leading_reactive,
        "Lagging_Current_Power_Factor": lagging_pf,
        "Leading_Current_Power_Factor": leading_pf,
        "WeekStatus": week_status,
        "Day_of_week": day_of_week,
        "NSM_sin": NSM_sin,
        "NSM_cos": NSM_cos,
        "day": day,
        "month_sin": month_sin,
        "month_cos": month_cos
    }])

    prediction = model.predict(input_df)[0]

    # Result Box
    st.markdown(f"""
    <div class="result-box">
        <b>Predicted Energy Consumption:</b> {prediction:.2f} kWh
    </div>
    """, unsafe_allow_html=True)

    # -----------------------------
    # Classification
    # -----------------------------
    threshold = 50

    if prediction >= threshold:
        st.markdown('<div class="high-box">High Energy Consumption 🔴</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="low-box">Low Energy Consumption 🟢</div>', unsafe_allow_html=True)

    # Insight line
    st.caption("This prediction helps monitor and optimize industrial energy usage.")