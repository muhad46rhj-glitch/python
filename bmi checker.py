h = float(input("Enter your height in cm: "))
w = float(input("Enter your weight in kg: "))

BMI = w/ (h/100)**2

print("your bmi is", BMI)

if BMI <= 18.4:
    print("your under weight.")
elif BMI <= 24.9:
    print("you are health.")
elif BMI <= 29.9:
    print("you are over weight.")
elif BMI <= 34.9:
    print("you are severly over weight.")
elif BMI <= 39.9:
    print("you are obese.")
else:
    print("you are severly obese.")