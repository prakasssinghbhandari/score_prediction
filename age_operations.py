



#   age = d2.year-d1 .year
 
#   if (d2.year,d2.day)<(d1.year,d1.day):
#     age-=1

  
#   return age

from datetime import datetime

def age_converter(d1, d2):
    age_years = d2.year - d1.year - ((d2.month, d2.day) < (d1.month, d1.day))
    age_months = (d2.month - d1.month - (d2.day < d1.day)) % 12
    age_days = (d2.day - d1.day) % 30

    return age_years, age_months, age_days

