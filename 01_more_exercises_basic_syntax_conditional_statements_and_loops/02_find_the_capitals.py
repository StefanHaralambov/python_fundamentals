word = input()

foo = ([pos for pos, char in enumerate(word) if char.isupper()])

print(foo)
