import streamlit as st
import numpy as np
import joblib

# Page configuration
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

# Load model and scaler
@st.cache_resource
def load_artifacts():
    model = joblib.load('heart_disease_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

model, scaler = load_artifacts()

st.title("🩺 Heart Disease Risk Prediction")
st.write("Enter the patient's clinical parameters below:")

# Form layout with two columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=50)
    sex = st.selectbox("Sex", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])

with col2:
    thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
    exang = st.selectbox("Exercise Induced Angina", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    oldpeak = st.number_input("ST Depression Induced by Exercise", 0.0, 10.0, 1.0, step=0.1)
    slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", [0, 1, 2])
    ca = st.selectbox("Major Vessels Colored by Fluoroscopy (0-4)", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia (1: Normal, 2: Fixed, 3: Reversible)", [1, 2, 3])

# Prediction trigger
# Prediction trigger
if st.button("Predict Risk", type="primary"):
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, 
                          thalach, exang, oldpeak, slope, ca, thal]])
    
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)[0]
    probabilities = model.predict_proba(scaled_features)[0]

    # In your dataset: index 0 is Disease, index 1 is Healthy
    prob_disease = probabilities[0] * 100
    prob_healthy = probabilities[1] * 100

    st.markdown("---")
    if prediction == 0:
        st.error(f"⚠️ **High Risk of Heart Disease** (Confidence: {prob_disease:.1f}%)")
    else:
        st.success(f"✅ **Low Risk / Healthy** (Confidence: {prob_healthy:.1f}%)")

st.caption("Disclaimer: This tool is built for educational/demonstration purposes only.")