import sys
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    weight = sys.argv[1]
    height = sys.argv[2]
    print("User provided input values:")
else:
    script_name = "bmi.py"
    weight = 1
    height = 1
    print("No input given - using default values:")

bmi = (float(weight) / (float(height) * float(height))) 

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"
print("Script Name:", script_name)
print("Weight (kg):", weight)
print("Height (m):", height)
print("BMI:", bmi)
print("Category:", category)
