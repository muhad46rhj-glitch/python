#take input for the student that he can attend the exam er not
madical_cause =  input("did you have a medical cause? (V/N): ").strip().upper()

#cheacking the user input and predicting output accordingly 
if madical_cause == "Y":   #codition 1
    print("You are allowed")
else:
    # take input of the attendence
    atten = int(input("Enter a attendence of students: "))

    if atten >= 75:  #condition 2
        print("Allowed")
    else:
        print("Not allowed")


