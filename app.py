import streamlit as st
import pickle
import pandas as pd

# Load the saved model pipeline
with open('Best_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Steel Industry Energy Consumption Prediction")

st.write("Enter the feature values below:")

# Input widgets
Usage_kWh = st.number_input("Usage_kWh")
Lagging_Current_Reactive = st.number_input("Lagging_Current_Reactive.Power_kVarh")
Leading_Current_Reactive = st.number_input("Leading_Current_Reactive_Power_kVarh")
CO2 = st.number_input("CO2(tCO2)")
Lagging_PF = st.number_input("Lagging_Current_Power_Factor")
Leading_PF = st.number_input("Leading_Current_Power_Factor")
WeekStatus = st.selectbox("WeekStatus", ["Weekday", "Weekend"])
Day_of_week = st.selectbox("Day_of_week", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
NSM_sin = st.number_input("NSM_sin")
NSM_cos = st.number_input("NSM_cos")
day = st.number_input("day", min_value=1, max_value=31)
month_sin = st.number_input("month_sin")
month_cos = st.number_input("month_cos")

# Predict button
if st.button("Predict"):
    # DataFrame for model
    input_df = pd.DataFrame([{
        "Usage_kWh": Usage_kWh,
        "Lagging_Current_Reactive.Power_kVarh": Lagging_Current_Reactive,
        "Leading_Current_Reactive_Power_kVarh": Leading_Current_Reactive,
        "CO2(tCO2)": CO2,
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
    
    # Prediction
    prediction = model.predict(input_df)
    st.success(f"Predicted Energy Usage: {prediction[0]:.2f}")