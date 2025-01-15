# import streamlit as st 
# from love_operations import check_love
# st.header("Love Calculator:")
# col1, col2 = st.columns(2)
# with col1:
#   name1=st.text_input("Enter your name:",placeholder="******",max_chars=10,label_visibility="visible")
# st.divider()
# with col2:
#  name2=st.text_input("Enter your partner name:",placeholder="******",max_chars=10)
# col1,col2,col3=st.columns(3)
# with col2:

#  if st.button("  calculate love",type="secondary"):
#   calculated_love=check_love(name1,name2)
#   st.info(f"According to love calculator {calculated_love}")

# import numpy as np
# with st.chat_message("user"):
#     if st.write("Hello 👋"):
#       st.text_input("")


# api_key = '05a527e19c834fc98687c2958bd5cfad'  
# url = f"https://api.exchangeratesapi.io/latest?access_key={api_key}"



import streamlit as st 
import requests
import json
st.header("Currency converter")
st.markdown("This changes the currencies")


api_key = '17ad30a6fbdef8b828e4e87feb6a2108'  
url = f"https://api.exchangeratesapi.io/latest?access_key={api_key}"

re=requests.get(url)
data=re.json()
# print(data)

country_names = list(data['rates'].keys()) 
print(country_names)

col1,col2,col3=st.columns(3)
with col1:

 currrency_1=st.selectbox("currency 1:",options=country_names)
with col2:
 st.markdown('<img src="https://i.ibb.co/CPrH0MV/exchanging.png" alt="exchanging" width="80" height="80" border="0">', unsafe_allow_html=True)

 

with col3:
  currency_2=st.selectbox("currency 2:",options=country_names)
# calc=country_names*data['rates']
# print(calc)
rate_1 = data['rates'][currrency_1]
rate_2=data['rates'][currency_2]
col1,col2,col3=st.columns(3)

amount = st.number_input("Enter the amount to convert:", min_value=0.0, format="%.2f")


converted_amount=(amount / rate_1) * rate_2

page_bg_color = """ 
<style> 
body { background-color: white; } 
</style> 
""" 
st.markdown(page_bg_color, unsafe_allow_html=True)


if st.button("convert"):
 st.status(f" {amount}  {currency_2}  is equal to {converted_amount} {currrency_1}",state="complete")
