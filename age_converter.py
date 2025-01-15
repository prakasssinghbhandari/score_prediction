import streamlit as st
import datetime
from age_operations import age_converter
d1= st.date_input("Enter your date of birth",format="YYYY/MM/DD")
d2=st.date_input("Today's Date",format="YYYY/MM/DD")
if st.button("convert"):
 your_age=age_converter(d1, d2)
 st.status(f"your age is{your_age}",expanded=False,state="complete")