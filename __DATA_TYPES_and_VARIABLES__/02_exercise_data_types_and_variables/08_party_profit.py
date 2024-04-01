group_size = int(input())
trip_time = int(input())

coins_count = 0

for day in range(1, trip_time + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    coins_count += 50 - 2 * group_size
    if day % 3 == 0:
        coins_count -= 3 * group_size
    if day % 5 == 0:
        coins_count += 20 * group_size
        if day % 3 == 0:
            coins_count -= 2 * group_size

coins_per_member = int(coins_count / group_size)

print(f"{group_size} companions received {coins_per_member} coins each.")
