number = int(input())

for row in range(1, number + 1):
    for empty_space in range(row, 0, -1):
        print("i", end="")
    for symbols in range(1, row + 1):
        print("*", end="")
    for x in range(row, 0, -1):
        print("j", end="")
    print()
