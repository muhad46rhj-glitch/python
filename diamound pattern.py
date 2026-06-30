# take input from user
rowSize = int(input("Enter the number of rows: "))

# Calculate half rows
if rowSize % 2 == 0:
    halfDiamRow = rowSize // 2
else:
    halfDiamRow = rowSize // 2 + 1

# Upper part
space = halfDiamRow - 1

for i in range(1, halfDiamRow + 1):
    # Print spaces
    for j in range(space):
        print(" ", end="")
    space -= 1

    # Print numbers
    num = 1
    for j in range(2 * i - 1):
        print(num, end="")
        num += 1
    print()

# Lower part
space = 1

for i in range(halfDiamRow - 1, 0, -1):
    # Print spaces
    for j in range(space):
        print(" ", end="")
    space += 1

    # Print numbers
    num = 1
    for j in range(2 * i - 1):
        print(num, end="")
        num += 1
    print()