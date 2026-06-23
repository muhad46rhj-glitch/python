#Input a word or sentence
string = input("please enter your own string : ")

string2 = ('')
#LOOP for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe original string = ", string)
print("the reverse string = ", string2)