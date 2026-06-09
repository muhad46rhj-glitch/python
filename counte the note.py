#talking total amount as input from user
Amount =int(input("Please Enter Amount for withdraw :"))

# Calculate the number of notes of diffrent dinominators
Note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("notes of 100 rupe" , Note_1)
print("notes of 50 rupe" , note_2)
print("notes of 10 rupe" , note_3)
