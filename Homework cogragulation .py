# String Operations Demo - Ready to Run

text = input("Enter a sentence or word: ")

print("\n--- String Operation Results ---")
print("1. Length:", len(text))
print("2. Uppercase:", text.upper())
print("3. Lowercase:", text.lower())
print("4. Title Case:", text.title())

if len(text) >= 3:
    print("5. First 3 chars:", text[:3])
    print("6. Last 3 chars:", text[-3:])

old = input("\nEnter character/word to replace: ")
new = input("Enter new character/word: ")
print("7. After replacement:", text.replace(old, new))

search = input("\nEnter substring to search for: ")
pos = text.find(search)
if pos != -1:
    print("8. Found at index:", pos)
else:
    print("8. Not found")

print("9. Split into words:", text.split())

sep = input("\nEnter separator (e.g., -, *, space): ")
print("10. Joined:", sep.join(text.split()))

start = input("\nCheck if starts with: ")
print("11. Starts with:", text.startswith(start))

end = input("Check if ends with: ")
print("12. Ends with:", text.endswith(end))

print("13. Stripped:", text.strip())

count_char = input("\nEnter character/word to count: ")
print("14. Count:", text.count(count_char))

name = input("\nEnter your name: ")
print(f"15. Message: Hello {name}, you wrote: '{text}'")

print("\n--- Program Complete ---")