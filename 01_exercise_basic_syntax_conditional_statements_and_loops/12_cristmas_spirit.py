decoration_quantity = int(input())
days_till_christmas = int(input())

price_ornament = 2  # points = 5
price_skirt = 5     # points = 3
price_garland = 3    # points = 10
price_lights = 15    # points = 17

money_spent = 0
christmas_spirit = 0

for day in range(1, days_till_christmas + 1):
    if day % 11 == 0:
        decoration_quantity += 2
    if day % 2 == 0:
        money_spent += price_ornament * decoration_quantity
        christmas_spirit += 5
    if day % 3 == 0:
        money_spent += (price_skirt + price_garland) * decoration_quantity
        christmas_spirit += 13
    if day % 5 == 0:
        money_spent += price_lights * decoration_quantity
        christmas_spirit += 17
    if day % 10 == 0:
        christmas_spirit -= 20
        money_spent += price_lights + price_garland + price_skirt
        if day % 10 == 0 and day == days_till_christmas:
            christmas_spirit -= 30
    if day % 15 == 0:
        christmas_spirit += 30

print(f"Total cost: {money_spent} \nTotal spirit: {christmas_spirit}")
