import streamlit as st 
from bmi_operations import calculate_bmi,bmi_remarks

st.header("BMI calculator")
weight=st.text_input("weight kg:",placeholder="enter your name",max_chars=10,value=60)
height=st.text_input("height:",placeholder="enter your height",max_chars=10,value=60)
print(weight)
print(height)
if st.button("calculate",help="click here to calculate BMI",type="primary"):
 BMI=calculate_bmi(float(weight),height)
 bmi_to_remarks=  bmi_remarks(BMI)
 st.status(f"your bmi is {BMI},{bmi_to_remarks}",expanded=False,state="complete")

#  print(calculate_bmi(float(weight),height))

