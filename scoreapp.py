import streamlit as st
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression


model_path = r'C:\Users\bhand\Downloads\gpa_prediction_model.pkl'
linear_model = joblib.load(model_path)


st.title("GPA Prediction App")
st.write("""
### Predict GPA based on Hours Per Day of Study
""")

hours_slider=st.slider("hours per day", min_value=0, max_value=24, label_visibility="visible")
hours_per_day = st.number_input("Enter the number of hours per day:", min_value=0.0, max_value=24.0, value=1.0, step=0.1)
if hours_slider != 0: 
    hours_per_day = hours_slider 
else: 
    hours_per_day = hours_per_day

if st.button("Predict GPA"):
    prediction = linear_model.predict([[hours_per_day]])

    max_gpa = 4
    capped_prediction = min(prediction[0], max_gpa)
    st.write(f"Predicted GPA: {capped_prediction:.2f}")
    
   

st.markdown( """ <a href="https://www.linkedin.com/in/prakash-bhandari-23559b334/" target="_blank"> <img src="https://i.imgur.com/3aLajp0.png" alt=prakass style="height: 24px; width: 24px;"> prakass </a> """, unsafe_allow_html=True )
