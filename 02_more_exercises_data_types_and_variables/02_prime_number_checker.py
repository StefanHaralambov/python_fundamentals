number = int(input())

is_prime = True

for num in range(2, number):
    for num_2 in range(2, number):
        if num * num_2 == number:
            is_prime = False
            break
    if not is_prime:
        break

print(is_prime)
