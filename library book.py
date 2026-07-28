# Library Book Availability Checker

books = ["Python", "Math", "Science", "English"]
copies = [3, 0, 5, 2]

# Pair book names with copy counts
library = dict(zip(books, copies))
print(library)

# Filter available books
available = list(filter(lambda x: x[1] > 0, library.items()))
print("Available:", available)

# Update late fees using map()
fees = [2, 4, 6, 8]
new_fees = list(map(lambda x: x + 1, fees))
print("Updated Fees:", new_fees)

# Combine values with zip()
combined = list(zip(books, new_fees))
print("Books & Fees:", combined)

# Stop program early when chosen book is found
choice = input("Enter book name: ")

for book in books:
    if book == choice:
        print(book, "is found!")
        break
else:
    print("Book not found.")