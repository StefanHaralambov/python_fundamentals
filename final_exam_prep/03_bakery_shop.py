in_stock = {}
food_sold = 0
while True:
    command = input().split()
    current_command = command[0]
    if current_command == "Complete":
        break

    if current_command == "Receive":
        quantity, food = int(command[1]), command[2]
        if quantity <= 0:
            continue
        if food not in in_stock:
            in_stock[food] = 0

        in_stock[food] += quantity

    if current_command == "Sell":
        quantity, food = int(command[1]), command[2]
        if food not in in_stock:
            print(f"You do not have any {food}.")
            continue
        if quantity <= int(in_stock[food]):
            print(f"You sold {quantity} {food}.")
            in_stock[food] -= quantity
            food_sold += quantity
        elif quantity > int(in_stock[food]):
            print(f"There aren't enough {food}. You sold the last {in_stock[food]} of them.")
            food_sold += int(in_stock[food])
            in_stock[food] = 0
        if in_stock[food] == 0:
            in_stock.pop(food)


for k, v in in_stock.items():
    print(f"{k}: {v}")
print(f"All sold: {food_sold} goods")
