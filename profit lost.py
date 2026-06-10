actual_cost = float(input(" please entre the actual product price: "))
sale_amount = float(input(" please entre the sale amount: "))

if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total profit = {0}".format (amount))
else:
    print("No profit!!!!")