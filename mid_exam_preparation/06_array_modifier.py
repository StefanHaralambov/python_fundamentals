lst_int = [int(x) for x in input().split()]

while True:
    command = input().split()
    type_command = command[0]

    if command[0] == "end":
        break

    elif type_command == "swap":
        index_1, index_2 = int(command[1]), int(command[2])
        lst_int[index_1], lst_int[index_2] = lst_int[index_2], lst_int[index_1]

    elif type_command == "multiply":
        index_1, index_2 = int(command[1]), int(command[2])
        lst_int[index_1] *= lst_int[index_2]

    elif type_command == "decrease":
        lst_int = [x - 1 for x in lst_int]

print(*lst_int, sep=", ")
