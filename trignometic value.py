import math  # importing math module

angle = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
radian = math.radians(angle)

# Calculate sin, cos, and tan
sin_value = math.sin(radian)
cos_value = math.cos(radian)
tan_value = math.tan(radian)

print("Sin(", angle, ") =", sin_value)
print("Cos(", angle, ") =", cos_value)
print("Tan(", angle, ") =", tan_value)