# BMI CALCULATOR

# person1
name1 = "Beryl"
height_m1 = 6.5
weight_kg1 = 56

#person2
name2 = "Marion"
height_m2 = 6.0
weight_kg2 = 53

#person3
name3 = "Belden"
height_m3 = 7.1
weight_kg3 = 75

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 30 :
        return name + " is not overweight"
    else:
        return name + " is overweight"
result1 = bmi_calculator( name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m1, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3) 


print(result1)
print(result2)
print(result3)