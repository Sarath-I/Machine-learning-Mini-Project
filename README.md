# 🛒 Online Shopper Revenue Prediction (ML + Web App)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge\&logo=streamlit)
![Status](https://img.shields.io/badge/Project-Production%20Ready-success?style=for-the-badge)

---

# 📌 Project Overview

This project builds a **machine learning classification system** to predict whether an online visitor will **generate revenue (purchase) or not**, based on their browsing behavior.

The project goes beyond model building by deploying the solution as an **interactive web application using Streamlit**, making it usable in real-world business scenarios such as **e-commerce analytics and customer targeting**.

---

# 🎯 Business Problem

E-commerce platforms need to identify **high-intent users** in real time.

This project helps answer:

* Which users are likely to make a purchase?
* How can businesses target potential buyers more effectively?
* How can user behavior data improve conversion rates?

---

# 🧠 Solution Approach

The solution combines:

* **Machine Learning Classification Model**
* **Feature Engineering & Preprocessing**
* **Model Deployment using Streamlit**

The system takes user session data as input and predicts **purchase intent instantly**.

---

# 📊 Features Used

The model uses behavioral and session-based features such as:

* Administrative & Informational page visits
* Product-related interactions
* Bounce Rate & Exit Rate
* Page Value
* Special Day impact
* Visitor Type (New/Returning)
* Month & Traffic-related features

These features help capture **user intent and engagement patterns**.

---

# ⚙️ Machine Learning Pipeline

## 1️⃣ Data Preprocessing

* Handled numerical and categorical features
* Applied **Label Encoding** for categorical variables (Month, VisitorType)
* Applied **Feature Scaling** using StandardScaler

---

## 2️⃣ Model Training

* Trained a **Random Forest Classifier** for prediction
* Saved model using **Pickle** for deployment

---

## 3️⃣ Model Deployment

The model is deployed using **Streamlit**:

* Interactive UI for user input
* Real-time prediction
* Clean and user-friendly interface

👉 The app takes multiple inputs and predicts:

* ✅ **Will Generate Revenue**
* ❌ **Will Not Generate Revenue**

---

# 🖥️ Web Application

The Streamlit app allows users to:

* Input session details
* Select categorical values dynamically
* Get instant predictions

Core implementation available in:
📄 

---

# 📁 Project Structure

```id="mlapp"
Online-Shopper-Revenue-Prediction
│
├── app.py                  # Streamlit web app
├── model.ipynb            # Model training notebook
│
├── dataset.csv            # Dataset
│
├── rf_model.pkl           # Trained model
├── scaler.pkl             # Feature scaler
├── le_month.pkl           # Label encoder (Month)
├── le_visitor.pkl         # Label encoder (VisitorType)
├── le_revenue.pkl         # Label encoder (Target)
│
├── requirements.txt       # Dependencies
└── README.md
```

---

# 🛠️ Technologies Used

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit
* Pickle (Model Serialization)

Dependencies listed in:
📄 

---

# 🚀 How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/Sarath-I/Machine-learning-Mini-Project.git
cd Machine-learning-Mini-Project
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App

```bash
streamlit run app.py
```

---

# 📊 Output

* Binary classification:

  * **True → Revenue Generated**
  * **False → No Revenue**

Displayed with clear UI indicators:

* ✅ Success message for positive prediction
* ❌ Error message for negative prediction

---

# 📈 Real-World Impact

This system can be used by:

* E-commerce platforms
* Marketing teams
* Product analysts

To:

* Improve **conversion rates**
* Optimize **targeted advertising**
* Enhance **user experience**

---


# 👨‍💻 Author

**Sarath**

Aspiring Data Scientist | Machine Learning Developer
Building real-world ML applications 🚀

---

⭐ If you found this project useful, consider **starring the repository**.
