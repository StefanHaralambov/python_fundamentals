letters = input().split(", ")

table_letters = {}

for i in range(len(letters)):
    number = ord(letters[i])
    char = letters[i]
    if char not in table_letters:
        table_letters[char] = number

print(table_letters)
