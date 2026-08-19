class Account:
    def __init__(self):
        self.username = "test_user"
        self.__password = "12345"
        self.__email = "private@example.com"


# Create account outside the class
account = Account()

print("===== PRIVATE ATTRIBUTE TEST =====")

# Public attribute
print("\nUsername:")
print(account.username)

# Direct access to private attributes
print("\nTrying direct password access:")

try:
    print(account.__password)
except AttributeError:
    print(" Cannot access __password directly")

print("\nTrying direct email access:")

try:
    print(account.__email)
except AttributeError:
    print(" Cannot access __email directly")


# Name-mangled access
print("\n===== NAME MANGLED TEST =====")

print("Password using name mangling:")
print(account._Account__password)

print("Email using name mangling:")
print(account._Account__email)