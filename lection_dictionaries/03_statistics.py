products = {}
while True:
    command = input().split(": ")
    if command[0] == "statistics":
        break
    key, value = command[0], int(command[1])
    if key not in products:
        products[key] = value
    else:
        products[key] += value
print("Products in stock:")
for (key, value) in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
