# Weekly Habit Tracker

habits = ("Exercise", "Reading", "Water")

print("Length:", len(habits))
print("First:", habits[0])
print("Slice:", habits[:2])

try:
    habits[0] = "Yoga"
except:
    print("Tuples cannot be changed.")