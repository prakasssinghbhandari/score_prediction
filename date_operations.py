# from datetime import timedelta
# def date_converter(d1, d2): 
  
#   age = d2- d1 
 
# #   years = age / 365 
  
#   return (age)
import streamlit as st
def money_exchange(Amount, option1, option2): 
    if option1 == "Nepali" and option2 == "Indian":
         exchanged_amount = Amount /1.6 
         return exchanged_amount 
    elif option1 == "Indian" and option2 == "Nepali": 
        exchanged_amount = Amount *1.6 
        return exchanged_amount 
    else:
         return "Invalid currency option"