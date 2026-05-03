# ⚡ Steel Industry Energy Consumption Prediction

## 📌 Project Overview

This project focuses on predicting **energy consumption in the steel industry** using multiple machine learning regression models. The goal is to build an accurate predictive system that can help optimize industrial energy usage.

---

## 🎯 Objective

* Predict energy consumption (kWh) based on operational parameters
* Compare multiple regression models
* Identify the best-performing model

---

## 📊 Dataset

* Industrial dataset with **35,000+ records**
* Key features:

  * Reactive Power (Lagging & Leading)
  * Power Factors
  * Time-based features (hour, day, month)
  * Week status (Weekday/Weekend)

---

## ⚙️ Feature Engineering

* Applied **cyclical encoding** for time-based features:

  * `NSM → sin/cos`
  * `Month → sin/cos`
* Improved model performance by preserving time patterns
* Handled categorical variables using encoding techniques

---

## 🤖 Models Used

* KNN Regressor
* Decision Tree Regressor
* Random Forest Regressor
* Linear Regression
* Support Vector Regressor
* AdaBoost Regressor
* Gradient Boosting
* XGBoost Regressor ⭐ (Best Model)

---

## 📈 Model Evaluation

* Evaluated using:

  * R² Score
  * RMSE (Root Mean Squared Error)
  * MAE (Mean Absolute Error)

👉 **XGBoost Regressor achieved the best performance**, with:

* Highest R² score
* Lowest prediction error

---

## 🚀 Deployment

* Built an interactive **Streamlit web app**
* Features:

  * User-friendly input interface
  * Real-time energy prediction

### App Link:https://steelindustryenergyconsumptionprediction-eqv8dkwsim8j7kpebbtee.streamlit.app/

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib
* XGBoost
* Streamlit

---

## 📌 Key Takeaways

* Tree-based ensemble models outperform linear models for this dataset
* Feature engineering (especially cyclical encoding) significantly improves accuracy
* Machine learning can effectively optimize industrial energy consumption

---
