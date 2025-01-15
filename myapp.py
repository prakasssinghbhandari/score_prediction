import streamlit as st 
# import datetime 
from date_operations import money_exchange
# d1= st.date_input("Enter your date of birth",format="YYYY-MM-DD")
# d2=st.date_input("Today's Date",format="YYYY-MM-DD")
# if st.button("convert"):
#  your_age=date_converter(d1, d2)
#  st.status(f"your age is{your_age}",expanded=False,state="complete")
st.header("Currency converter:")
col1,col2,col3=st.columns(3)
with col1:
 Amount= st.number_input(
    "Amount:", value=10, placeholder="enter money to be converted...,",min_value=0)
 option1=st.selectbox("currency to be converted ⤵", key="visibility", options=["Nepali", "Indian"] )  
with col2:
 option2=st.selectbox( "Currency to be converted in 👉", options=["Indian", "Nepali","" ], )
st.divider()

if st.button("calculate",type="primary"):
  money_exchanged=money_exchange(Amount,option1,option2)
  st.info(f"the exchanged amount is: {money_exchanged}")
 

