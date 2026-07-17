# Student Marks List Analyzer

marks = [78, 85, 92, 67, 88]

print("Marks:", marks)
print("Length:", len(marks))
print("First:", marks[0])
print("Last:", marks[-1])
print("Slice:", marks[1:4])

for mark in marks:
    print(mark)

print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Smallest:", min(marks))
print("Largest:", max(marks))