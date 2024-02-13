lost_fights_quantity = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())

expenses = 0
shield_broken_count = 0

for fight in range(1, lost_fights_quantity + 1):
    if fight % 2 == 0:
        expenses += price_helmet
    if fight % 3 == 0:
        expenses += price_sword
    if fight % 3 == 0 and fight % 2 == 0:
        expenses += price_shield
        shield_broken_count += 1
        if shield_broken_count == 2:
            expenses += price_armor
            shield_broken_count = 0


print(f"Gladiator expenses: {expenses:.2f} aureus")
