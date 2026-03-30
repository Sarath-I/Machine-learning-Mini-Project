import streamlit as st
import pandas as pd
import pickle

# Load models
model = pickle.load(open("rf_model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

le_month = pickle.load(open("le_month.pkl","rb"))
le_visitor = pickle.load(open("le_visitor.pkl","rb"))
le_revenue = pickle.load(open("le_revenue.pkl","rb"))

st.title("Online Shopper Revenue Prediction")

Administrative = st.number_input("Administrative",0)
Administrative_Duration = st.number_input("Administrative_Duration",0.0)
Informational = st.number_input("Informational",0)
Informational_Duration = st.number_input("Informational_Duration",0.0)
ProductRelated = st.number_input("ProductRelated",0)
ProductRelated_Duration = st.number_input("ProductRelated_Duration",0.0)
BounceRates = st.number_input("BounceRates",0.0)
ExitRates = st.number_input("ExitRates",0.0)
PageValues = st.number_input("PageValues",0.0)
SpecialDay = st.number_input("SpecialDay",0.0)

Month = st.selectbox("Month", le_month.classes_)
OperatingSystems = st.number_input("OperatingSystems",1)
Browser = st.number_input("Browser",1)
Region = st.number_input("Region",1)
TrafficType = st.number_input("TrafficType",1)
VisitorType = st.selectbox("VisitorType", le_visitor.classes_)
Weekend = st.selectbox("Weekend",[0,1])

# Encode categorical
Month = le_month.transform([Month])[0]
VisitorType = le_visitor.transform([VisitorType])[0]

input_data = pd.DataFrame([[Administrative, Administrative_Duration, Informational,
                            Informational_Duration, ProductRelated, ProductRelated_Duration,
                            BounceRates, ExitRates, PageValues, SpecialDay, Month,
                            OperatingSystems, Browser, Region, TrafficType, VisitorType, Weekend]],
                          columns=['Administrative','Administrative_Duration','Informational',
                                   'Informational_Duration','ProductRelated','ProductRelated_Duration',
                                   'BounceRates','ExitRates','PageValues','SpecialDay','Month',
                                   'OperatingSystems','Browser','Region','TrafficType','VisitorType','Weekend'])

input_scaled = scaler.transform(input_data)

if st.button("Predict"):
    pred = model.predict(input_scaled)
    result = le_revenue.inverse_transform(pred)

    if result[0] == "True":
        st.success("✅ This visitor WILL generate revenue")
    else:
        st.error("❌ This visitor will NOT generate revenue")
