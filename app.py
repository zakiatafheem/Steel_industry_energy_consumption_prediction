import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(
    page_title="Steel Energy Predictor",
    page_icon="⚡",
    layout="wide"
)

# Load model
with open('Best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtitle {
        font-size: 18px;
        color: #7f8c8d;
    }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">⚡ Steel Industry Energy Consumption Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Predict energy usage based on operational parameters</p>', unsafe_allow_html=True)

# Sidebar Inputs
st.sidebar.header("🔧 Input Parameters")

Usage_kWh = st.sidebar.number_input("Usage (kWh)", value=50.0)
Lagging_Current_Reactive = st.sidebar.number_input("Lagging Reactive Power (kVarh)")
Leading_Current_Reactive = st.sidebar.number_input("Leading Reactive Power (kVarh)")
Lagging_PF = st.sidebar.number_input("Lagging Power Factor")
Leading_PF = st.sidebar.number_input("Leading Power Factor")

WeekStatus = st.sidebar.selectbox("Week Status", ["Weekday", "Weekend"])
Day_of_week = st.sidebar.selectbox("Day of Week", 
                                  ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

NSM_sin = st.sidebar.number_input("NSM (sin)")
NSM_cos = st.sidebar.number_input("NSM (cos)")
day = st.sidebar.number_input("Day", min_value=1, max_value=31)
month_sin = st.sidebar.number_input("Month (sin)")
month_cos = st.sidebar.number_input("Month (cos)")

# Layout sections
col1, col2 = st.columns(2)

with col1:
    st.subheader("⚙️ Operational Inputs")
    st.write(f"**Usage (kWh):** {Usage_kWh}")
    st.write(f"**Day:** {day}")
    st.write(f"**Week Status:** {WeekStatus}")

with col2:
    st.subheader("🔋 Electrical Parameters")
    st.write(f"**Lagging Reactive Power:** {Lagging_Current_Reactive}")
    st.write(f"**Leading Reactive Power:** {Leading_Current_Reactive}")
    st.write(f"**Lagging PF:** {Lagging_PF}")
    st.write(f"**Leading PF:** {Leading_PF}")

st.divider()

# Prediction Button
if st.button("🚀 Predict Energy Consumption"):
    
    input_df = pd.DataFrame([{
        "Usage_kWh": Usage_kWh,
        "Lagging_Current_Reactive.Power_kVarh": Lagging_Current_Reactive,
        "Leading_Current_Reactive_Power_kVarh": Leading_Current_Reactive,
        "Lagging_Current_Power_Factor": Lagging_PF,
        "Leading_Current_Power_Factor": Leading_PF,
        "WeekStatus": WeekStatus,
        "Day_of_week": Day_of_week,
        "NSM_sin": NSM_sin,
        "NSM_cos": NSM_cos,
        "day": day,
        "month_sin": month_sin,
        "month_cos": month_cos
    }])

    prediction = model.predict(input_df)

    st.success("✅ Prediction Completed!")

    # Highlight result
    st.metric(
        label="⚡ Predicted Energy Usage",
        value=f"{prediction[0]:.2f} kWh"
    )

    # Optional interpretation
    if prediction[0] > 100:
        st.warning("⚠️ High Energy Consumption Detected")
    else:
        st.info("ℹ️ Energy Consumption is within normal range")