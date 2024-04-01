import re

furniture = []
total_price = 0
pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"
while True:
    purchase = input()
    if purchase == "Purchase":
        break
    check = re.findall(pattern, purchase)
    if check:
        for items in check:
            furniture.append(items[0])
            total_price += float(items[1]) * int(items[2])

print("Bought furniture:")
for i in furniture:
    print(i)
print(f"Total money spend: {total_price:.2f}")
