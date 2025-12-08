# Churn ->           1 Yes 0 No
# Gender ->          1 Female 0 Male
# Dependents ->      1 Yes 0 No
# Contract ->        2 Two year 1 One year 0 Month-to-Month
# X_train_test is saved as scaler.pkl
# Best model is saved as model.pkl
# Order of X  -> 'gender', 'tenure', 'MonthlyCharges', 'Dependents', 'Contract'

import numpy as np
import streamlit as st
import joblib

scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

st.title('Churn Prediction Model')

st.divider()

st.write('Please input values and click on the Predict button')

gender = st.selectbox('Please select a Gender', ['Male', 'Female'])
tenure = st.number_input('Please input a Tenure value', min_value=0, max_value=130, value=10)
MonthyCharges = st.number_input('Please input a Monthly value', min_value=30, max_value=150, value=60)
Dependents = st.selectbox('Please select Depedency category', ['Yes', 'No'])
Contract = st.selectbox('Please select a Contract type',['Month-to-Month', 'One-year', 'Two year'])

st.divider()

predictbutton = st.button('Predict')

if predictbutton:
    gender_selected = 1 if gender == 'Female' else 0
    contract_selected = 0 if Contract == 'Month-to-month' else (1 if Contract == 'One year' else 2)
    dependent_selected = 1 if Dependents == 'Yes' else 0
    X = (gender_selected, tenure, MonthyCharges, dependent_selected, contract_selected)
    X1 = np.array(X)
    X_array = scaler.transform([X1])
    
    prediction = model.predict(X_array)
    predicted = 'Likely to lose customer' if prediction == 1 else 'Customer will be likely retained'

    st.write(predicted)

else:
    st.write('Please enter values and hit the Predict button')
    



