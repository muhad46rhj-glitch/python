def add(P,Q):
    #this function used for add in two numbers
    return P + Q
def subtract(P, Q):
    # this function is using for subtracting two numbers
    return P - Q
def multiply(P , Q):
    #this function is using for multipling two number
    return P * Q
def divide(P, Q):
    #this function is used dividing two numbers
    return P / Q

# now we will take inputs from the uesr
print ("please select this operator.")
print("a. Add")
print("b. subtract")
print("c. multiply")
print("d. Divide")

choice = input("please enter choice (a/ b/ c/ d): ")

num_1 = int (input("please enter the first number: "))
num_2 = int (input("please enter the secound number: "))

if choice == 'a':
    print (num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == 'b':
    print (num_1, " - ", num_2,  "= ", subtract(num_1, num_2))

elif choice == 'c':
    print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))

elif choice == 'd':
    print (num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("this is an invaild input")
