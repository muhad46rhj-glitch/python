print("Selected your ride: ")
print("1.bike")
print("2.car")

#take input of number 1or2
#Select your ride
choice = int(input("enter your choice: "))

#user entering option 1
if( choice == 1): #codition 1 outer if statement
    print(" what type of the bike? " )
    print("1 scoty\n")
    print("2 scotter\n")

   #codition for selecting the type of  bike
    choice2=int(input("enter your choice2: "))
    if choice2==1: #inner if statement
     print("you have selected scooty")
    else:
     print("you have select scooter")

    #User entering option 2
elif( choice == 2 ): #outer elif statement
  print(" what type of car?" )
  print("1.seden")
  print("2.xuv")
  choice3=int(input("enter your choice3: "))

  if choice3==1: #inner if statement
  #codition for selececting the type of car
    print("you have selected seden")
  else:
    print("you have selected a xuv")

else: #outer else statement
   print("wrong choice!")