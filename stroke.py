import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🧠 Stroke Prediction App")

# User input (raw)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.slider("Age", 0, 100, 30)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
ever_married = st.selectbox("Ever Married", ["Yes", "No"])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
Residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=100.0)
bmi = st.number_input("BMI", min_value=0.0, value=25.0)
smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

# Manual label encoding (same mapping used during training)
gender_map = {"Male": 1, "Female": 0, "Other": 2}
ever_married_map = {"Yes": 1, "No": 0}
work_type_map = {"Private": 2, "Self-employed": 3, "Govt_job": 0, "children": 1, "Never_worked": 4}
Residence_type_map = {"Urban": 1, "Rural": 0}
smoking_status_map = {"formerly smoked": 0, "never smoked": 1, "smokes": 2, "Unknown": 3}

# Encoded values
input_df = pd.DataFrame([{
    'gender': gender_map[gender],
    'age': age,
    'hypertension': hypertension,
    'heart_disease': heart_disease,
    'ever_married': ever_married_map[ever_married],
    'work_type': work_type_map[work_type],
    'Residence_type': Residence_type_map[Residence_type],
    'avg_glucose_level': avg_glucose_level,
    'bmi': bmi,
    'smoking_status': smoking_status_map[smoking_status]
}])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.error("⚠️ High Risk: This person may have a stroke.")
    else:
        st.success("✅ Low Risk: This person is unlikely to have a stroke.")