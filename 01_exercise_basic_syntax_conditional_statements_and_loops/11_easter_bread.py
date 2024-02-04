budget = float(input())
price_flour_1kg = float(input())
colored_eggs = 0
bread_count = 0
money_left = budget

price_eggs = 0.75 * price_flour_1kg
price_milk_250ml = 1.25 * price_flour_1kg / 4
price_for_1_loaf = price_eggs + price_milk_250ml + price_flour_1kg
loaf_count = 0

while money_left >= price_for_1_loaf:
    bread_count += 1
    loaf_count += 1
    colored_eggs += 3
    money_left -= price_for_1_loaf
    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2


print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")

