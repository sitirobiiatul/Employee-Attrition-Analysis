# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1diIwWPAXCE3HIgL3TH4H8LPLasU4-FhZ
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from joblib import load
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Load model
model = joblib.load('gb_model.joblib')

# Preprocessing function
def data_preprocessing(data_input):
    df = pd.read_csv('cleaned_employee_data.csv')
    df = df.drop(columns=['EmployeeId', 'Attrition', 'StandardHours'], errors='ignore')
    df = pd.concat([df, data_input], ignore_index=True)

    numerical = df.select_dtypes(exclude='object').columns.tolist()
    categorical = df.select_dtypes(include='object').columns.tolist()

    df[categorical] = df[categorical].apply(LabelEncoder().fit_transform)
    df[numerical] = MinMaxScaler().fit_transform(df[numerical])

    return df.tail(1)

# Streamlit Interface
st.title("🎯 Employee Attrition Prediction")

with st.form("employee_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", 18, 60, 30)
        business_travel = st.selectbox("Business Travel", ['Non-Travel', 'Travel_Rarely', 'Travel_Frequently'])
        daily_rate = st.number_input("Daily Rate", 100, 1500, 800)
        department = st.selectbox("Department", ['Sales', 'Research & Development', 'Human Resources'])
        distance_from_home = st.slider("Distance From Home", 1, 30, 5)
        education = st.selectbox("Education", ['Below College', 'College', 'Bachelor', 'Master', 'Doctor'])
        education_field = st.selectbox("Education Field", ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other', 'Human Resources'])

    with col2:
        environment_satisfaction = st.selectbox("Environment Satisfaction", ['Low', 'Medium', 'High', 'Very High'])
        gender = st.radio("Gender", ['Male', 'Female'])
        hourly_rate = st.number_input("Hourly Rate", 30, 100, 50)
        job_involvement = st.selectbox("Job Involvement", ['Low', 'Medium', 'High', 'Very High'])
        job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
        job_role = st.selectbox("Job Role", ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                             'Manufacturing Director', 'Healthcare Representative', 'Manager',
                                             'Sales Representative', 'Research Director', 'Human Resources'])
        job_satisfaction = st.selectbox("Job Satisfaction", ['Low', 'Medium', 'High', 'Very High'])

    with col3:
        marital_status = st.selectbox("Marital Status", ['Single', 'Married', 'Divorced'])
        monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
        monthly_rate = st.number_input("Monthly Rate", 2000, 30000, 15000)
        num_companies_worked = st.slider("Num Companies Worked", 0, 10, 2)
        over_time = st.selectbox("OverTime", ['Yes', 'No'])
        percent_salary_hike = st.slider("Percent Salary Hike", 10, 25, 15)
        performance_rating = st.selectbox("Performance Rating", ['Low', 'Good', 'Excellent', 'Outstanding'])

    relationship_satisfaction = st.selectbox("Relationship Satisfaction", ['Low', 'Medium', 'High', 'Very High'])
    stock_option_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])
    total_working_years = st.slider("Total Working Years", 0, 40, 10)
    training_times_last_year = st.selectbox("Training Times Last Year", [0, 1, 2, 3, 4, 5, 6])
    work_life_balance = st.selectbox("Work Life Balance", ['Low', 'Good', 'Excellent', 'Outstanding'])
    years_at_company = st.slider("Years at Company", 0, 40, 5)
    years_in_current_role = st.slider("Years in Current Role", 0, 18, 3)
    years_since_last_promotion = st.slider("Years Since Last Promotion", 0, 15, 1)
    years_with_curr_manager = st.slider("Years with Current Manager", 0, 17, 3)

    submitted = st.form_submit_button("🔍 Predict")

# Prediction
if submitted:
    input_df = pd.DataFrame([{
        'Age': age,
        'BusinessTravel': business_travel,
        'DailyRate': daily_rate,
        'Department': department,
        'DistanceFromHome': distance_from_home,
        'Education': education,
        'EducationField': education_field,
        'EnvironmentSatisfaction': environment_satisfaction,
        'Gender': gender,
        'HourlyRate': hourly_rate,
        'JobInvolvement': job_involvement,
        'JobLevel': job_level,
        'JobRole': job_role,
        'JobSatisfaction': job_satisfaction,
        'MaritalStatus': marital_status,
        'MonthlyIncome': monthly_income,
        'MonthlyRate': monthly_rate,
        'NumCompaniesWorked': num_companies_worked,
        'OverTime': over_time,
        'PercentSalaryHike': percent_salary_hike,
        'PerformanceRating': performance_rating,
        'RelationshipSatisfaction': relationship_satisfaction,
        'StockOptionLevel': stock_option_level,
        'TotalWorkingYears': total_working_years,
        'TrainingTimesLastYear': training_times_last_year,
        'WorkLifeBalance': work_life_balance,
        'YearsAtCompany': years_at_company,
        'YearsInCurrentRole': years_in_current_role,
        'YearsSinceLastPromotion': years_since_last_promotion,
        'YearsWithCurrManager': years_with_curr_manager
    }])

    processed = data_preprocessing(input_df)
    prediction = model.predict(processed)[0]
    probas = model.predict_proba(processed)[0][1]

    if prediction == 1:
        st.error(f"🚨 Employee is likely to leave. (Probability: {probas:.2f})")
    else:
        st.success(f"✅ Employee is likely to stay. (Probability of leaving: {probas:.2f})")

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>© 2025 | Developed by <strong>Siti Robiiatul Adawiyyah</strong></p>", unsafe_allow_html=True)
