temperature = float(input("Enter the temperature (°C): "))

if temperature < 15:
    print("The weather is Cold.")
elif temperature < 30:
    print("The weather is Warm.")
else:
    print("The weather is Hot.")