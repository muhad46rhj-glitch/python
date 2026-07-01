secret = 27
lives =5

while lives > 0:
    guess = int(input("enter your number(1-50):"))

    if guess == secret:
        print("your guessed it!")
        break
    elif abs(guess - secret) <= 2:
        print("hot")
    elif abs(guess - secret) <= 10:
        print("cold")
    else:
        print("ice cold")

    lives-=1
    print("lives:","heart"* lives)

if lives == 0:
    print("Game Over!")
    print("The secret number was",secret)