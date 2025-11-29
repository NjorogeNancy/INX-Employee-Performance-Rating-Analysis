import streamlit as st
import pandas as pd
import numpy as np
import pickle

#loading the saved model
with open("Random_Forest_Model.pkl", "rb") as f:
    model = pickle.load(f)


st.title("INX Future Inc Employee Performance Predictor App")
st.write("This app predicts employee performance rating based on key features")

#inputs
st.header("Enter Empyoyee's Details")

#mappings

gender_map = {"Male": 1, "Female": 0}
education_bg_map = {"Technical degree":0,"Marketing":1,"Life Sciences":2,"Medical":3,"Human Resources":4,"Other":5}
marital_map = {"Single":0, "Married":1, "Divorced":2}
department_map = {"Development":0,"Sales":1,"Human Resource":2,"Data Science":3,"Research and Development":4,"Finance":5}
job_role_map = {
    "Business Analyst":0,"Senior Developer":1,"Sales Representative":2,"Delivery Manager":3,"Finance Manager":4,
    "Technical Architect":5,"Manager":6,"Healthcare Representative":7,"Laboratory Technician":8,"Sales Executive":9,
    "Developer":10,"Technical Lead":11,"Senior ManagerR&D":12,"Manufacturing Director":13,"Manager R&D":14,
    "Data Scientist":15,"Human Resources":16,"Research Director":17,"Research Scientist":18
}
travel_map = {"Non-Travel":0,"Travel_Rarely":1,"Travel_Frequently":2}
education_level_map = {"Below College":1,"College":2,"Bachelor":3,"Master":4,"Doctor":5}
env_satisfaction_map = {"Low":1,"Medium":2,"High":3,"Very High":4}
job_involvement_map = {"Low":1,"Medium":2,"High":3,"Very High":4}
job_satisfaction_map = {"Low":1,"Medium":2,"High":3,"Very High":4}
overtime_map = {"No":0,"Yes":1}
relationship_map = {"Low":1,"Medium":2,"High":3,"Very High":4}
worklife_map = {"Bad":1,"Good":2,"Better":3,"Best":4}
attrition_map = {"No":0,"Yes":1}

#userinputs

age = st.number_input("Age", min_value=18, max_value=60)

gender_label = st.selectbox("Gender", list(gender_map.keys()))
gender = gender_map[gender_label]

education_background_label = st.selectbox("Education Background", list(education_bg_map.keys()))
education_background = education_bg_map[education_background_label]

marital_status_label = st.selectbox("Marital Status", list(marital_map.keys()))
marital_status = marital_map[marital_status_label]

emp_department_label = st.selectbox("Department", list(department_map.keys()))
emp_department = department_map[emp_department_label]

emp_job_role_label = st.selectbox("Job Role", list(job_role_map.keys()))
emp_job_role = job_role_map[emp_job_role_label]

business_travel_label = st.selectbox("Business Travel Frequency", list(travel_map.keys()))
business_travel = travel_map[business_travel_label]

distance_from_home = st.number_input("Distance From Home", min_value=0, max_value=50)

emp_education_level_label = st.selectbox("Education Level", list(education_level_map.keys()))
emp_education_level = education_level_map[emp_education_level_label]

emp_env_satisfaction_label = st.selectbox("Environment Satisfaction", list(env_satisfaction_map.keys()))
emp_env_satisfaction = env_satisfaction_map[emp_env_satisfaction_label]

emp_hourly_rate = st.number_input("Hourly Rate", min_value=0, max_value=150)

emp_job_involvement_label = st.selectbox("Job Involvement", list(job_involvement_map.keys()))
emp_job_involvement = job_involvement_map[emp_job_involvement_label]

emp_job_level = st.number_input("Job Level", min_value=1, max_value=5)

emp_job_satisfaction_label = st.selectbox("Job Satisfaction", list(job_satisfaction_map.keys()))
emp_job_satisfaction = job_satisfaction_map[emp_job_satisfaction_label]

num_companies_worked = st.number_input("Num Companies Worked", min_value=0, max_value=10)

overtime_label = st.selectbox("OverTime", list(overtime_map.keys()))
overtime = overtime_map[overtime_label]

salary_hike = st.number_input("Last Salary Hike Percent", min_value=0, max_value=30)

emp_relationship_sat_label = st.selectbox("Relationship Satisfaction", list(relationship_map.keys()))
emp_relationship_sat = relationship_map[emp_relationship_sat_label]

total_work_experience = st.number_input("Total Work Experience (Years)", min_value=0, max_value=40)

training_times_last_year = st.number_input("Training Times Last Year", min_value=0, max_value=20)

emp_worklife_balance_label = st.selectbox("WorkLife Balance", list(worklife_map.keys()))
emp_worklife_balance = worklife_map[emp_worklife_balance_label]

exp_years_company = st.number_input("Experience Years at Company", min_value=0, max_value=40)

exp_years_current_role = st.number_input("Experience Years in Current Role", min_value=0, max_value=40)

years_since_last_promotion = st.number_input("Years Since Last Promotion", min_value=0, max_value=20)

years_with_manager = st.number_input("Years With Current Manager", min_value=0, max_value=20)

attrition_label = st.selectbox("Attrition", list(attrition_map.keys()))
attrition = attrition_map[attrition_label]

#model inputs
input_data = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "EducationBackground": [education_background],
    "MaritalStatus": [marital_status],
    "EmpDepartment": [emp_department],
    "EmpJobRole": [emp_job_role],
    "BusinessTravelFrequency": [business_travel],
    "DistanceFromHome": [distance_from_home],
    "EmpEducationLevel": [emp_education_level],
    "EmpEnvironmentSatisfaction": [emp_env_satisfaction],
    "EmpHourlyRate": [emp_hourly_rate],
    "EmpJobInvolvement": [emp_job_involvement],
    "EmpJobLevel": [emp_job_level],
    "EmpJobSatisfaction": [emp_job_satisfaction],
    "NumCompaniesWorked": [num_companies_worked],
    "OverTime": [overtime],
    "EmpLastSalaryHikePercent": [salary_hike],
    "EmpRelationshipSatisfaction": [emp_relationship_sat],
    "TotalWorkExperienceInYears": [total_work_experience],
    "TrainingTimesLastYear": [training_times_last_year],
    "EmpWorkLifeBalance": [emp_worklife_balance],
    "ExperienceYearsAtThisCompany": [exp_years_company],
    "ExperienceYearsInCurrentRole": [exp_years_current_role],
    "YearsSinceLastPromotion": [years_since_last_promotion],
    "YearsWithCurrManager": [years_with_manager],
    "Attrition": [attrition],
})

#predictions
if st.button("Predict Performance Rating"):
    prediction = model.predict(input_data)[0]
    st.write(f"### Predicted Performance Rating: **{prediction}**")



































































































