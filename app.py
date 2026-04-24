import streamlit as st
import pandas as pd
import pickle

# Load Model

@st.cache_resource
def load_model():
    with open("best_model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# Page Config

st.set_page_config(page_title="Steel Energy Predictor", layout="wide")

st.title("⚡ Steel Industry Energy Consumption Predictor")
st.markdown("Predict energy usage based on operational and electrical inputs")


# Sidebar Inputs

st.sidebar.header("🔧 Input Parameters")

day = st.sidebar.number_input("Day of Month", 1, 31, 10)

week_status = st.sidebar.selectbox("Week Status", ["Weekday", "Weekend"])
day_of_week = st.sidebar.selectbox("Day of Week", 
                                  ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

# Electrical Inputs
lagging_reactive = st.sidebar.number_input("Lagging Reactive Power (kVarh)", value=0.0)
leading_reactive = st.sidebar.number_input("Leading Reactive Power (kVarh)", value=0.0)

lagging_pf = st.sidebar.number_input("Lagging Power Factor", value=0.0)
leading_pf = st.sidebar.number_input("Leading Power Factor", value=0.0)

# Time Features
nsm = st.sidebar.number_input("NSM (Seconds from Midnight)", value=0.0)

# Feature Engineering

diff = lagging_reactive - leading_reactive

week_status_val = 1 if week_status == "Weekend" else 0

day_map = {
    "Monday":1, "Tuesday":2, "Wednesday":3,
    "Thursday":4, "Friday":5, "Saturday":6, "Sunday":7
}
day_val = day_map[day_of_week]

# Create Input DataFrame

input_df = pd.DataFrame({
    "Day_of_month": [day],
    "WeekStatus": [week_status_val],
    "Day_of_week": [day_val],
    "Lagging_Current_Reactive_Power_kVarh": [lagging_reactive],
    "Leading_Current_Reactive_Power_kVarh": [leading_reactive],
    "Lagging_Current_Power_Factor": [lagging_pf],
    "Leading_Current_Power_Factor": [leading_pf],
    "NSM": [nsm],
    "diff": [diff]  
})

# Layout

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Input Overview")
    st.dataframe(input_df)

with col2:
    st.subheader("⚡ Prediction")

    if st.button("Predict Energy Consumption"):
        try:
            prediction = model.predict(input_df)[0]
            st.success(f"🔋 Predicted Energy Consumption: {prediction:.2f} kWh")
        except Exception as e:
            st.error(f"Error: {e}")
