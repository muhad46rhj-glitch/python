def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("enter the secound number: "))
    op = input("enter operation(+,-,*,/,):")

    if op =="+":
        print("Answer:",add(num1,num2))
    elif op =="-":
        print("Answer:",subtract(num1,num2))
    elif op =="*":
        print("Answer:",multiply(num1,num2))
    elif op =="/":
        print("Answer:",divide(num1,num2))
    else:
        print("Invaild operation")
except ValueError:
    print("Invaild number")
except ZeroDivisionError:
    print("cannot divide by zero")

