import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

password = ""

for i in range(length):
    password += random.choice(characters)

print("Random Password:", password)