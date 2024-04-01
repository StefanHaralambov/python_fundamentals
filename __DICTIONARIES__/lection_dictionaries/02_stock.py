products = input().split()
targets = input().split()

groceries = {}

for items in range(0, len(products), 2):
    key = products[items]
    value = products[items + 1]
    groceries[key] = int(value)

for item in targets:
    if item in groceries:
        print(f"We have {groceries[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
