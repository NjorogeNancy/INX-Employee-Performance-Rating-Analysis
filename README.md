

# **Employee Performance Prediction — INX Future Inc.**

A complete end-to-end machine learning project that analyzes employee data to understand key performance drivers and build a predictive model for employee **PerformanceRating**.
The model is later deployed via Streamlit to assist HR teams in evaluating potential hires and improving workforce performance.

---

## **Project Overview**

INX Future Inc. aims to identify factors affecting employee performance and use predictive analytics to support decision-making in recruitment and workforce development.
This project delivers:

### **1. Department-wise Performance Analysis**

Analyzes which departments show high, average, or low performance trends.

### **2. Top 3 Factors Influencing Performance**

Discovers the strongest predictors using EDA, correlation, feature importance, and HR logic.

### **3. A Machine Learning Model to Predict Performance**

Trains and compares three models:

* Logistic Regression (baseline)
* Decision Tree
* Random Forest (best model)

### **4. Recommendations for HR & Management**

Actionable insights based on data patterns to improve employee performance.

---

## **Dataset Description**

**Dataset:** INX_Future_Inc_Employee_Performance_CDS_Project2_Data
**Rows:** ~1200
**Columns:** ~28

Includes:

* Demographics (Age, Gender, Marital Status)
* Job details (Job Level, Department, Job Role)
* Experience metrics (Total Experience, Experience in Company, Promotion history)
* Satisfaction metrics (Job Satisfaction, Work-Life Balance, Environment Satisfaction)
* Salary details
* Target variable: **PerformanceRating** (1–4)

Ordinal attributes were encoded using meaningful numerical codes.

---

## **Exploratory Data Analysis**

### **Univariate Analysis**

* Most employees rated “Good” and “Excellent”
* Balanced gender distribution
* A majority fall within mid-career ranges (5–15 years of total experience)

### **Bivariate Analysis**

Key findings include:

* Higher **job level**, **experience**, and **satisfaction scores** show strong links to higher performance.
* Early-career employees are more prone to lower ratings.
* R&D shows more consistent high performance compared to Sales & HR.

### **Multivariate Analysis**

A correlation heatmap revealed:

* Strong cluster between Total Work Experience, Experience at Company, and Job Level
* Salary closely tied to Job Level and Experience
* Weak correlation for DistanceFromHome, YearsSinceLastPromotion, etc.

---

## **Machine Learning Approach**

### **Models Trained**

1. **Logistic Regression**

   * Baseline linear model for interpretability
2. **Decision Tree Classifier**

   * Non-linear, easy to interpret but prone to overfitting
3. **Random Forest Classifier**

   * Ensemble method that reduced overfitting & captured complex relations
   * Achieved **best performance**

### **Why Random Forest Was Chosen**

* Handles mixed data types
* Manages non-linear relationships
* Robust to noise
* Built-in handling of class imbalance (via class weights)
* Produces feature importance ranking
* Best macro F1-score and accuracy among tested models

### **Top Performance Predictors**

1. **Total Work Experience in Years**
2. **EmpJobLevel**
3. **EmpJobSatisfaction**

These align strongly with HR domain understanding and EDA conclusions.

---

## **Model Performance (Summary)**

| Model               | Strength                   | Weakness                | Performance |
| ------------------- | -------------------------- | ----------------------- | ----------- |
| Logistic Regression | Simple, interpretable      | Poor on non-linear data | Lowest      |
| Decision Tree       | Captures thresholds        | Overfits                | Moderate    |
| **Random Forest**   | Accurate, stable, balanced | Less interpretable      | **Best**    |

Final model achieved high accuracy and strong macro F1 score across classes.

---

## **Business Recommendations**

Based on analysis:

### **1. Strengthen Early-Career Development**

New employees show lower performance → improve onboarding & mentorship.

### **2. Improve Job Satisfaction**

High satisfaction strongly predicts high performance → invest in recognition, autonomy, and role alignment.

### **3. Support Sales Department Consistency**

Sales shows wider performance swings → provide targeted coaching & analytics tools.

### **4. Career Progression Clarity**

Employees at higher job levels perform better → establish transparent career pathways.

---

## **How to Run the Project Locally**

### **Requirements**

Install dependencies:

```bash
pip install -r requirements.txt
```

### **Running the Jupyter Notebook**

```bash
jupyter notebook
```

Open the main notebook:

```
Data Analysis.ipynb
```

---

## **Streamlit App Deployment**

### **Run Streamlit Locally**

```bash
streamlit run app.py
```

### **app.py Responsibilities**

* Load saved `.pkl` model
* Take employee feature inputs
* Process through the pipeline
* Output predicted performance category

---

## **Project Structure**

```
.
├── employee_perf_modeling.ipynb     # Full EDA + Modeling
├── app.py                           # Streamlit app
├── Random_Forest_Model.pkl   # Saved best model 
├── README.md                        # Project documentation
├── requirements.txt                 # Libraries used
└── data/
    └── INX_Future_Inc_Employee_Performance_CDS.csv
```

---

## **Technologies Used**

* Python
* Jupyter Notebook
* Pandas, NumPy
* Scikit-learn
* Seaborn + Matplotlib
* Streamlit


---

## **Author**

**Nancy** 
