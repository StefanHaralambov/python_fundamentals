number_of_strings = int(input())

for string in range(number_of_strings):
    current_string = input()
    is_pure = True
    for char in current_string:
        if char == "_" or char == "," or char == ".":
            is_pure = False
            break
    if not is_pure:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure!")
