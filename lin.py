# Step 3: Create a Streamlit application script
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

st.title('Salary Prediction App')

st.write('Enter the years of experience to predict the salary.')

# Get user input for experience
experience = st.number_input('Years of Experience', min_value=0.0, format="%f")

# Predict the salary
if st.button('Predict'):
    # The model expects a 2D array
    predicted_salary = model.predict(np.array([[experience]]))
    st.write(f'Predicted Salary: ${predicted_salary[0]:,.2f}')