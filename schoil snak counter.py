from array import array

# Sets
snacks1 = {"Chips", "Juice", "Cake"}
snacks2 = {"Cake", "Biscuit", "Juice"}

# Add new snack
snacks1.add("Candy")

# Shared snacks
print("Shared Snacks:", snacks1 & snacks2)

# Array
counts = array('i', [10, 20, 30])

# Add values
counts.append(20)
counts.append(40)

# Count and reverse
print("Count of 20:", counts.count(20))

counts.reverse()
print("Reversed Array:", counts)