# 🏥 Hospital Readmission Prediction

A machine learning project that predicts whether a diabetic patient is likely to be **readmitted to the hospital within 30 days** based on clinical, demographic, medication, diagnosis, and hospital-related information.

The project uses the **UCI Diabetes 130-US Hospitals for Years 1999–2008** dataset and compares multiple machine learning classification models, including Logistic Regression, Random Forest, and XGBoost.

---

## 📌 Project Overview

Hospital readmissions can increase healthcare costs and indicate the need for additional patient care and monitoring.

This project focuses on building a binary classification system that predicts:

* `0` → No 30-Day Readmission
* `1` → 30-Day Readmission

The project includes data understanding, cleaning, preprocessing, model training, evaluation, feature importance analysis, and a Streamlit-based prediction interface.

---

## 🎯 Objectives

* Understand the structure and quality of the hospital dataset.
* Perform data cleaning and missing-value handling.
* Handle categorical and numerical features appropriately.
* Address class imbalance during model training.
* Train and compare multiple classification models.
* Evaluate models using appropriate classification metrics.
* Analyze important features using XGBoost feature importance.
* Build an interactive Streamlit application for prediction.

---

## 📊 Dataset

**Dataset:** Diabetes 130-US Hospitals for Years 1999–2008

The dataset contains approximately **101,766 hospital encounters** and includes information such as:

* Patient demographics
* Hospital admission details
* Length of hospital stay
* Laboratory procedures
* Medical procedures
* Medication information
* Diagnosis codes
* Previous inpatient visits
* Previous emergency visits
* Previous outpatient visits
* Number of diagnoses

### Target Variable

The original `readmitted` column contains multiple readmission categories.

A binary target was created:

```python
readmitted_30 = (readmitted == "<30").astype(int)
```

Therefore:

```text
0 → No 30-Day Readmission
1 → 30-Day Readmission
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* XGBoost

### Visualization

* Matplotlib
* Seaborn

### Model Serialization

* Joblib

### Deployment

* Streamlit

### Development Environment

* Jupyter Notebook
* Python Virtual Environment

---

## 🔄 Project Workflow

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
Missing Value Handling
     ↓
Feature Selection
     ↓
Train/Test Split
     ↓
Feature Preprocessing
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Comparison
     ↓
Feature Importance Analysis
     ↓
Final XGBoost Model
     ↓
Streamlit Application
```

---

## 🧹 Data Preprocessing

### Removed Columns

Columns with extremely high missing-value percentages or identifiers that were not useful for prediction were removed.

Examples include:

```text
weight
medical_specialty
payer_code
encounter_id
patient_nbr
max_glu_serum
A1Cresult
```

### Missing Values

For selected categorical columns, missing values were represented as:

```text
Unknown
```

### Numerical Features

Numerical features were standardized using:

```python
StandardScaler()
```

### Categorical Features

Categorical features were converted into numerical representation using:

```python
OneHotEncoder(
    handle_unknown="ignore"
)
```

A `ColumnTransformer` was used to apply the appropriate preprocessing to each feature type.

---

## ⚖️ Handling Class Imbalance

The target variable is imbalanced, with 30-day readmissions representing a minority of the dataset.

To reduce the effect of this imbalance:

### Logistic Regression

```python
class_weight="balanced"
```

### Random Forest

```python
class_weight="balanced"
```

### XGBoost

The positive-class weighting was calculated using:

```python
scale_pos_weight = negative_count / positive_count
```

This helps the models give greater importance to the minority class.

---

## 🤖 Models Used

Three classification models were trained and evaluated.

### 1. Logistic Regression

Used as the baseline model because it is simple, interpretable, and provides a useful reference for more complex models.

### 2. Random Forest

An ensemble tree-based model capable of learning nonlinear relationships between features.

### 3. XGBoost

A gradient-boosting algorithm designed for high-performance learning on structured/tabular datasets.

---

## 📈 Model Performance

| Model               | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| Logistic Regression |   0.6456 |    0.1674 | 0.5478 |   0.2565 |  0.6426 |
| Random Forest       |   0.8886 |    0.6111 | 0.0048 |   0.0096 |  0.6605 |
| XGBoost             |   0.6664 |    0.1862 | 0.5905 |   0.2831 |  0.6848 |

Because the dataset is highly imbalanced, accuracy was not considered in isolation. Recall, F1-score, and ROC-AUC were also examined.

XGBoost produced the highest ROC-AUC and recall among the evaluated models and was used as the final model for the application.

---

## 🔍 XGBoost Feature Importance

Feature importance analysis was performed to understand which encoded features contributed most to the model.

The highest-ranked features included:

```text
number_inpatient
discharge_disposition_id
diag_1_V57
diag_1_715
diag_2_342
diag_1_V58
diag_3_286
diag_1_428
```

`number_inpatient` had the highest individual feature importance among the encoded features in the trained XGBoost model.

Because categorical variables were one-hot encoded, a single original variable such as `diag_1` can appear as multiple encoded features.

---

## 🖥️ Application Features

The Streamlit application includes inputs for:

* Patient demographics
* Admission information
* Hospital stay information
* Diagnosis information
* Medication information
* Diabetes medication status
* Previous hospital visits

The application returns:

```text
Prediction:
30-Day Readmission
or
No 30-Day Readmission

Readmission Probability:
XX.XX%
```

---

## 🧠 Key Machine Learning Concepts Demonstrated

This project demonstrates practical implementation of:

* Exploratory Data Analysis
* Missing-value analysis
* Feature engineering
* Train-test splitting
* Stratified sampling
* Feature scaling
* One-hot encoding
* Pipeline-based preprocessing
* Imbalanced classification
* Logistic Regression
* Random Forest
* XGBoost
* Confusion Matrix
* Precision
* Recall
* F1 Score
* ROC-AUC
* Feature importance
* Model serialization
* Streamlit deployment

---

## ⭐ Project Highlights

* End-to-end healthcare machine learning project
* Handles imbalanced binary classification
* Compares three different ML approaches
* Uses a complete preprocessing + model pipeline
* Includes model evaluation and feature importance analysis
* Provides an interactive Streamlit prediction interface
