basket1 = {"apple","banana","mango", "apple","grapes"}
basket2 = {"mango","kiwi","banana", "kiwi"}
print("basket 1:", basket1)
print("basket 2:", basket2)

basket1.add("orange")
print("basket 1 after adding orange:",basket1)

common_fruits = basket1.intersection(basket2)
print("fruits in both baskets:", common_fruits)

import array as arr
fruit_counts = arr.array('i',[3,5,2,4])
print("fruit counts array:", fruit_counts)

fruit_counts.insert(0, 1)
fruit_counts.append(6)
print("fruit counts after adding items:",fruit_counts)

count_of_4= fruit_counts.count(4)
print("number of times 4 appears:", count_of_4)

fruit_counts.reverse()
print("reversed fruit count array:", fruit_counts)

print("")
print("===== Class fruit basket organizer =====")
print("basket 1:", basket1)
print("basket 2:", basket2)
print("shared fruits:", common_fruits)
print("fruit counts:", fruit_counts)
print("==================================")