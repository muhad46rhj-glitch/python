# Smart Command Device

print("=== SMART COMMAND DEVICE ===")
print("Type 'help' to see commands.")
print("Type 'exit' to stop.")

light = False
fan = False

while True:
    command = input("\nEnter command: ").lower()

    if command == "light on":
        light = True
        print("💡 Light is ON")

    elif command == "light off":
        light = False
        print("💡 Light is OFF")

    elif command == "fan on":
        fan = True
        print("🌀 Fan is ON")

    elif command == "fan off":
        fan = False
        print("🌀 Fan is OFF")

    elif command == "temperature":
        print("🌡️ Temperature is 22°C")

    elif command == "status":
        print("\n--- Device Status ---")
        print("Light:", "ON" if light else "OFF")
        print("Fan:", "ON" if fan else "OFF")

    elif command == "help":
        print("\nAvailable commands:")
        print("light on")
        print("light off")
        print("fan on")
        print("fan off")
        print("temperature")
        print("status")
        print("exit")

    elif command == "exit":
        print("Smart device shutting down...")
        break

    else:
        print("❌ Unknown command. Type 'help'.")