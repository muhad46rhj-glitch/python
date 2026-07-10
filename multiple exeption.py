try:
    num1 , num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)
   #using multiple exception block of diffrent type of error

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("comma is missing. Enter numbers separated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("NO exception")

finally:
    print("This will excecute no metter what")