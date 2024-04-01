snowballs_quantity = int(input())

best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0
best_snowball_value = 0


for snowball in range(1, snowballs_quantity + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = (weight / time) ** quality

    if snowball_value > best_snowball_value:
        best_snowball_value = int(snowball_value)
        best_snowball_weight = weight
        best_snowball_time = time
        best_snowball_quality = quality

print(f"{best_snowball_weight} : {best_snowball_time} = {best_snowball_value} ({best_snowball_quality})")
