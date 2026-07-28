item = ["pencil", "eraser", "notebook", "shapener", "glue"]
stock_counts = [12, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(item, stock_counts)}
print("full Inventory:", inventory)

in_stock_items = [item for item in item if inventory [item] > 0]
print("Items in Stock", in_stock_items)

chose_item = input("which item do you want to buy? ")

if chose_item not in inventory or inventory[chose_item] == 0:
    print(chose_item, "is out of stock! Stopping the checker.")
    exit()

prices = [10, 5, 40, 15, 20]
marked = int(input("enter the markup amount to add to every price: "))

marked_up_prices = list(map(lambda p: p + marked, prices))
print("Marked Up Prices:", marked_up_prices)

item_index = item.index(chose_item)
chose_price = marked_up_prices[item_index]
print("price of", chose_item, "after markup:", chose_price)

inventory[chose_item] = inventory [chose_item] -1
print(chose_item, "purchased! remaining stock:", inventory[chose_item])

print("")
print("===== School Store Inventory Checker =======")
print("Item Bought:", chose_item)
print("price paid:", chose_price)
print("updated inventory:", inventory)
print("=============================================")