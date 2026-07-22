# Student Subject Record Cleaner

students = {
    "Ali": "Math",
    "Sara": "English",
    "Ahmed": "Science"
}

print(students.get("Ali"))   # Safe access

students["John"] = "Computer"    # Add
students["Sara"] = "Physics"     # Update

students.pop("Ahmed")            # Remove

print("Length:", len(students))

for name, subject in students.items():
    print(name, ":", subject)