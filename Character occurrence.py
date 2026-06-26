#take input of a word
string = input("please enter your own word : ")
#take input of a character
char = input("please enter your own character : ")
i = 0
count = 0
#loop will to find the occurece of character
while(i < len(string)): #string opreation

    if(string[i] == char): # condition 1
        count = count + 1
    i = i + 1

#display the result
print("the total number of times ", char, "has occurred = " , count)