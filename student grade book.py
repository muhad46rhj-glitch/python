students = {
    "Ali":30,
    "Ahmad":50,
    "Sara":60,
    "Ayesha":70,
    "Zain":80,
}
total = 0
for score in students.values():
    total += score
print("Class Average:",total /len(students))
high = max(students,key=students.get)
low = min(students,key=students.get)

print("higest:", high, students[high])
print("lowest:", low, students[low])

name = input("Enter student name:")
print("score:", students.get(name,"Student not found"))