import streamlit as st
import pandas as pd
import joblib

st.title("Prediksi Harapan Hidup")

schooling = st.slider("Schooling", 0.0, 20.0, 12.0)
gdp = st.number_input("GDP", value=5000.0)
bmi = st.slider("BMI", 10.0, 40.0, 22.0)
alcohol = st.slider("Alcohol", 0.0, 15.0, 5.0)

model = joblib.load("model_regresi.pkl")

if st.button("Prediksi"):
    data = pd.DataFrame({
        "Schooling": [schooling],
        "GDP": [gdp],
        "BMI": [bmi],
        "Alcohol": [alcohol]
    })
    pred = model.predict(data)[0]
    st.success(f"Prediksi Harapan Hidup: {pred:.2f} tahun")
