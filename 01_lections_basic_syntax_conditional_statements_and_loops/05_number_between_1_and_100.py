number = float(input())

not_in_range = True

while not_in_range:
    if 1 <= number <= 100:
        not_in_range = False
        break
    number = float(input())

print(f"The number {number} is between 1 and 100")
