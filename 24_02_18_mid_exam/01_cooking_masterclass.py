import math

budget = float(input())
students = int(input())

price_package_flour = float(input())
price_egg = float(input())
price_apron = float(input())

floor_discount = students // 5
sum_price_flour = (students - floor_discount) * price_package_flour

quantity_apron = math.ceil(students * 1.2)
sum_price_apron = quantity_apron * price_apron

quantity_eggs = students * 10
sum_price_eggs = quantity_eggs * price_egg

cost = sum_price_eggs + sum_price_apron + sum_price_flour

if budget >= cost:
    print(f"Items purchased for {cost:.2f}$.")
else:
    needed_money = cost - budget
    print(f"{needed_money:.2f}$ more needed.")
