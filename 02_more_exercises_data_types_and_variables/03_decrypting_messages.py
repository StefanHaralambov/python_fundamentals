key = int(input())
lines = int(input())

secret_phrase = ""

for index in range(lines):
    letter = input()
    int_letter = ord(letter)
    new_letter = chr(key + int_letter)
    secret_phrase += new_letter

print(secret_phrase)
