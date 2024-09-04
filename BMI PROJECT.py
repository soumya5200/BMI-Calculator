# Get user input for height in cm and weight in kg
height_cm = float(input("Enter your height in cm: "))
weight_kg = float(input("Enter your weight in kg: "))

# Convert height from cm to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight_kg / height_m**2

# Determine and print BMI category
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are severely overweight.")




# password generator
# import random
# import string
# print("password generator")
# length = int(input("enter the length of password"))
# uppercase = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# lowercase = ("abcdefghijk") 
# digit = ("12345567789")
# symbol = ("@,%,&,*,(),$")
# all = uppercase+lowercase+digit+symbol
# password = random.sample(all,length)
# password = "".join(password)
# print("password is",password)

              
