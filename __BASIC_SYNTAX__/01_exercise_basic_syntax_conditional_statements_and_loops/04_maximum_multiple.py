divisor_number = int(input())
boundary_number = int(input())

for number in range(boundary_number, divisor_number, -1):
    if number % divisor_number == 0:
        print(number)
        break
