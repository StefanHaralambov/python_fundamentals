command = int(input())


def print_of_number(sum_of_digits_):
    print(f"{number} -> {is_special}")


for number in range(1, command + 1):
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True
        print_of_number(sum_of_digits)

    else:
        is_special = False
        print_of_number(sum_of_digits)
