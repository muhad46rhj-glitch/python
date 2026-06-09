# Square Root Calculator
print("Welcome to Square Root Calculator")
print("-" * 30)

num = float(input("Enter a number: "))

if num > 0:
    result = num ** 0.5
    print("Square root:", result)
elif num == 0:
    result = 0
    print("Square root:", result)
else:
    print("Error: Cannot calculate square root of negative number!")

print("-" * 30)
print("Thank you for using!")