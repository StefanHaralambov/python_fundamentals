max_numbers = int(input())

for quantity in range(max_numbers):
    number = int(input())
    if not number % 2 == 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")
