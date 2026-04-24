import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title=" Steel Energy Predictor",
    page_icon="⚡",
    layout="wide"
)
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

/* Title */
.title {
    font-size: 50px;
    font-weight: 800;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 17px;
    color: #6c7a89;
}

/* Card */
.card {
    background: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
    width: 100%;
    border: none;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">⚡ Steel Energy Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Single dashboard for input overview + energy prediction</p>', unsafe_allow_html=True)

st.divider()

st.sidebar.header("🔧 Input Panel")

day = st.sidebar.number_input("Day of Month", 1, 31, value=10)

WeekStatus = st.sidebar.selectbox("Week Status", ["Weekday", "Weekend"])

Day_of_week = st.sidebar.selectbox(
    "Day of Week",
    ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
)

st.sidebar.subheader("⚡ Electrical Data")
Lagging_Current_Reactive = st.sidebar.number_input("Lagging Reactive Power (kVarh)")
Leading_Current_Reactive = st.sidebar.number_input("Leading Reactive Power (kVarh)")
Lagging_PF = st.sidebar.number_input("Lagging Power Factor")
Leading_PF = st.sidebar.number_input("Leading Power Factor")

st.sidebar.subheader("📅 Time Features")
NSM_sin = st.sidebar.number_input("NSM sin")
NSM_cos = st.sidebar.number_input("NSM cos")
month_sin = st.sidebar.number_input("Month sin")
month_cos = st.sidebar.number_input("Month cos")


col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Overview")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("⚙️ **Operational Data**")
    st.write(f"Day of Month: {day}")
    st.write(f"Week Status: {WeekStatus}")
    st.write(f"Day of Week: {Day_of_week}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("⚡ **Electrical Data**")
    st.write(f"Lagging Reactive Power: {Lagging_Current_Reactive}")
    st.write(f"Leading Reactive Power: {Leading_Current_Reactive}")
    st.write(f"Lagging PF: {Lagging_PF}")
    st.write(f"Leading PF: {Leading_PF}")
    st.markdown('</div>', unsafe_allow_html=True)


with col2:
    st.subheader("🔮 Prediction")

    st.info("Click below to predict energy consumption")

    if st.button("⚡ Predict Energy Usage"):

        input_df = pd.DataFrame([{
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

        prediction = model.predict(input_df)[0]

        st.success("Prediction Completed!")

        st.metric("⚡ Energy Consumption :", f"{prediction:.2f} kWh")

        # Interpretation
        if prediction > 100:
            st.error("🔥 High Energy Usage")
            st.progress(0.85)
        elif prediction > 60:
            st.warning("⚠️ Moderate Energy Usage")
            st.progress(0.55)
        else:
            st.success("✅ Low Energy Usage")
            st.progress(0.25)