
def eligibility_check(salary,time,rate):
    
    monthly_interest_rate = rate / 12 / 100
    

    loan_tenure_months = time * 12
    
   
    max_emi = salary*0.44677
    max_loan = (max_emi * ((1 + monthly_interest_rate)**loan_tenure_months - 1)) / \
               (monthly_interest_rate * (1 + monthly_interest_rate)**loan_tenure_months)
    
    return max_loan
def emi(salary,time,rate):
    
    monthly_interest_rate = rate / 12 / 100
    loan_tenure_months = time * 12
    max_emi = salary*0.44677
    max_loan = (max_emi * ((1 + monthly_interest_rate)**loan_tenure_months - 1)) / \
               (monthly_interest_rate * (1 + monthly_interest_rate)**loan_tenure_months)
    emi = (max_loan * monthly_interest_rate * (1 + monthly_interest_rate)**loan_tenure_months) / \
          ((1 + monthly_interest_rate)**loan_tenure_months - 1)
    
    return  emi



