def calculate_bmi(weight,height):
    height_in_square_meter= (float(height)*0.0254)**2
    BMI=weight/height_in_square_meter
    return round(BMI,2)
def bmi_remarks(BMI):
    if BMI >18.5:
        print("under weight")
    if 18.5<BMI>24.9:
        print("normal")
    if 25.0<BMI>29.0:
        print("overweight")
    else:
       return"obese"
    
        