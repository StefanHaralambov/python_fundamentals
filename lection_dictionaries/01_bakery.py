products = input().split(" ")

groceries = {}

for items in range(0, len(products), 2):
    key = products[items]
    value = products[items + 1]
    groceries[key] = int(value)

print(groceries)
