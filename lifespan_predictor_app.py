import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('lifespan_predictor_model.pkl')

# Title and description
st.title("Lifespan Prediction App")
st.write("This app predicts lifespan based on age, sex, smoking habits, height, and weight.")

# User input form
st.header("Enter the details:")

age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ["Female", "Male"])
smoking = st.selectbox("Smoking Habit", ["Non-Smoker", "Smoker"])
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

# Convert inputs to the format expected by the model
sex_binary = 1 if sex == "Male" else 0
smoking_binary = 1 if smoking == "Smoker" else 0

input_data = pd.DataFrame({
    'Age': [age],
    'Sex': [sex_binary],
    'Smoking': [smoking_binary],
    'Height': [height],
    'Weight': [weight]
})

# Predict button
if st.button("Predict Lifespan"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Lifespan: {prediction[0]:.2f} years")

st.write("### Note:")
st.write("This prediction is based on simulated data and should not be considered medically accurate.")

