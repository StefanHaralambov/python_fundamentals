max_symbols = int(input())

for y in range(1, max_symbols + 1):
    for symbols in range(1, max_symbols + 1):

        if y == max_symbols:
            print("*", end="")
        elif y != 1 and max_symbols != symbols != 1:
            print(" ", end="")
        else:
            print("*", end="")

    print(" " * max_symbols)
    print("")
