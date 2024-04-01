max_symbols = int(input())

for row in range(1, max_symbols + 1):
    for symbols in range(row):
        print("*", end="")
    print()
for row in range(max_symbols - 1, 0, -1):
    for symbols in range(row):
        print("*", end="")
    print()
