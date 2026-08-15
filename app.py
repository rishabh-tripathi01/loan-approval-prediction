import streamlit as st
import pickle
import numpy as np

# Model load karo
with open('loan_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Loan Approval Prediction")
st.write("Apni details daalo aur turant prediction dekho")

# User se saare inputs lo
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0, value=5000)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0, value=0)
loan_amount = st.number_input("Loan Amount", min_value=0, value=100)
loan_amount_term = st.number_input("Loan Amount Term (in days)", min_value=0, value=360)
credit_history = st.selectbox("Credit History", ["1 (Good)", "0 (Bad)"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

if st.button("Predict"):
    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    dependents_val = 3 if dependents == "3+" else int(dependents)
    education_val = 0 if education == "Graduate" else 1
    self_employed_val = 1 if self_employed == "Yes" else 0
    credit_history_val = 1 if credit_history == "1 (Good)" else 0
    
    property_map = {"Rural": 0, "Semiurban": 1, "Urban": 2}
    property_val = property_map[property_area]
    
    input_data = np.array([[gender_val, married_val, dependents_val, education_val,
                             self_employed_val, applicant_income, coapplicant_income,
                             loan_amount, loan_amount_term, credit_history_val, property_val]])
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("Loan Approved! ✅")
    else:
        st.error("Loan Rejected ❌")
st.markdown("---")
st.markdown("Built by **Rishabh Tripathi** | B.Tech CS (AI & DS)")
st.markdown("[View on GitHub](https://github.com/rishabh-tripathi01/loan-approval-prediction)")
