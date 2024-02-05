word = input()

# foo = ([pos for pos, char in enumerate(word) if char.isupper()])

# print(foo)

pos = []

for letter, char in enumerate(word):
    if char.isupper():
        pos.append(letter)

print(pos)
