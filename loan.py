import streamlit as st 
from loan_operations import eligibility_check,emi
st.header("Loan Eligibility Checker:")
col1,col2,=st.columns(2)
with col1:
 st.selectbox("Type of loan:",options=["Home loan","car loan","education loan"])
 salary=st.number_input("Enter your monthly salary")
with col2:
 time=st.number_input("Loan terms (years):",value=1)
 rate=st.number_input("Interest rate%:",value=6)
maximum_loan=eligibility_check(salary,time,rate)
maximum_emi=emi(salary,time,rate)

col1,col2,col3=st.columns(3)
with col2:
 if st.button("check"):
    st.status(f"you can borrow up to :   {maximum_loan}",expanded=False,state="complete")
    st.status(f"your emi will be :   {maximum_emi}",expanded=False,state="complete")
# print(emi(maximum_loan,time,rate))
print(emi(salary,time,rate))
