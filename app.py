import streamlit as st
import numpy as np
import pickle
import json
import os

# -----------------------------------------
# PATH SETUP
# -----------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")

# -----------------------------------------
# LOAD MODELS
# -----------------------------------------
diabetes_model = pickle.load(open(os.path.join(MODELS_DIR, "diabetes_model.pkl"), "rb"))
diabetes_scaler = pickle.load(open(os.path.join(MODELS_DIR, "diabetes_scaler.pkl"), "rb"))

heart_model = pickle.load(open(os.path.join(MODELS_DIR, "heart_model.pkl"), "rb"))
heart_scaler = pickle.load(open(os.path.join(MODELS_DIR, "heart_scaler.pkl"), "rb"))

with open(os.path.join(MODELS_DIR, "lifestyle_tips.json")) as f:
    lifestyle_tips = json.load(f)

# -----------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_lifestyle_recommendations(user):
    recs = []

    bmi = user["BMI"]
    recs += lifestyle_tips["BMI"][bmi_category(bmi)]

    if user["Smoking"] == "Yes":
        recs += lifestyle_tips["Smoking"]["Yes"]

    if user["AlcoholDrinking"] == "Yes":
        recs += lifestyle_tips["AlcoholDrinking"]["Yes"]

    if user["PhysicalActivity"] == "No":
        recs += lifestyle_tips["PhysicalActivity"]["No"]

    if user["SleepTime"] < 6:
        recs += lifestyle_tips["SleepTime"]["Low"]
    elif user["SleepTime"] > 9:
        recs += lifestyle_tips["SleepTime"]["High"]

    if user["Diabetic"] == "Yes":
        recs += lifestyle_tips["Diabetic"]["Yes"]

    if user["HeartDisease"] == "Yes":
        recs += lifestyle_tips["HeartDisease"]["Yes"]

    if user["Stroke"] == "Yes":
        recs += lifestyle_tips["Stroke"]["Yes"]

    return list(dict.fromkeys(recs))

# -----------------------------------------
# STREAMLIT UI
# -----------------------------------------
st.set_page_config(page_title="Smart Health Assistant", page_icon="🩺", layout="wide")

st.sidebar.title("🩺 Smart Health Assistant")
page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Diabetes Prediction", "Heart Disease Prediction", "BMI & Lifestyle", "About"]
)

# -----------------------------------------
# HOME
# -----------------------------------------
if page == "Home":
    st.title("🏥 Smart Health Assistant")
    st.markdown("""
    AI-powered health prediction system using Machine Learning.

    **Features**
    - Diabetes Risk Prediction  
    - Heart Disease Prediction  
    - BMI Calculation  
    - Lifestyle Recommendations  
    """)

# -----------------------------------------
# DIABETES PREDICTION
# -----------------------------------------
elif page == "Diabetes Prediction":
    st.title("🩸 Diabetes Risk Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Pregnancies", 0, 20, 2)
        Glucose = st.number_input("Glucose", 0, 300, 120)
        BloodPressure = st.number_input("Blood Pressure", 0, 200, 70)

    with col2:
        SkinThickness = st.number_input("Skin Thickness", 0, 100, 20)
        Insulin = st.number_input("Insulin", 0, 900, 79)
        BMI = st.number_input("BMI", 1.0, 60.0, 28.5)

    with col3:
        DPF = st.number_input("Diabetes Pedigree Function", 0.0, 5.0, 0.47)
        Age = st.number_input("Age", 1, 120, 45)

    if st.button("Predict Diabetes"):
        glucose_bmi = Glucose / BMI
        insulin_glucose = Insulin / Glucose

        x = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                       Insulin, BMI, DPF, Age, glucose_bmi, insulin_glucose]])

        x_scaled = diabetes_scaler.transform(x)
        pred = diabetes_model.predict(x_scaled)[0]

        if pred == 1:
            st.error("⚠ High Risk of Diabetes")
        else:
            st.success("🟢 Low Risk of Diabetes")

# -----------------------------------------
# HEART DISEASE PREDICTION
# -----------------------------------------
elif page == "Heart Disease Prediction":
    st.title("❤️ Heart Disease Prediction")

    inputs = []
    labels = [
        "Age", "Sex (1=Male,0=Female)", "Chest Pain", "Resting BP",
        "Cholesterol", "Fasting Sugar", "Rest ECG", "Max Heart Rate",
        "Exercise Angina", "Oldpeak", "Slope", "CA", "Thal"
    ]

    for label in labels:
        inputs.append(st.number_input(label))

    if st.button("Predict Heart Disease"):
        x = np.array(inputs).reshape(1, -1)
        x_scaled = heart_scaler.transform(x)
        pred = heart_model.predict(x_scaled)[0]

        if pred == 1:
            st.error("⚠ High Risk of Heart Disease")
        else:
            st.success("🟢 Low Risk of Heart Disease")

# -----------------------------------------
# BMI & LIFESTYLE
# -----------------------------------------
elif page == "BMI & Lifestyle":
    st.title("⚖️ BMI & Lifestyle Recommendations")

    weight = st.number_input("Weight (kg)", 20, 200, 70)
    height = st.number_input("Height (cm)", 50, 230, 170)

    Smoking = st.selectbox("Smoking", ["Yes", "No"])
    AlcoholDrinking = st.selectbox("Alcohol Drinking", ["Yes", "No"])
    PhysicalActivity = st.selectbox("Physical Activity", ["Yes", "No"])
    SleepTime = st.number_input("Sleep Hours", 0, 24, 7)
    Diabetic = st.selectbox("Diabetic", ["Yes", "No"])
    HeartDisease = st.selectbox("Heart Disease", ["Yes", "No"])
    Stroke = st.selectbox("Stroke", ["Yes", "No"])

    if st.button("Get Results"):
        bmi = calculate_bmi(weight, height)
        st.info(f"BMI: {bmi} ({bmi_category(bmi)})")

        user = {
            "BMI": bmi,
            "Smoking": Smoking,
            "AlcoholDrinking": AlcoholDrinking,
            "PhysicalActivity": PhysicalActivity,
            "SleepTime": SleepTime,
            "Diabetic": Diabetic,
            "HeartDisease": HeartDisease,
            "Stroke": Stroke
        }

        tips = get_lifestyle_recommendations(user)

        st.subheader("Lifestyle Recommendations")
        for tip in tips:
            st.write("✔", tip)

# -----------------------------------------
# ABOUT
# -----------------------------------------
elif page == "About":
    st.title("ℹ️ About Project")
    st.markdown("""
    **Smart Health Assistant**

    - Machine Learning based health prediction system  
    - Streamlit-powered interactive UI  
    - Diabetes & Heart Disease Prediction  
    - BMI & Lifestyle Recommendation Engine  

    **Tech Stack:** Python, Streamlit, Scikit-learn  
    """)
