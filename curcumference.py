import math

# Function to calculate circumference
def circumference(radius):
    return 2 * math.pi * radius

# Get input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the circumference
result = circumference(radius)
print("The circumference of the circle is:", result)
