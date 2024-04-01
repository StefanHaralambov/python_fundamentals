lines = int(input())
sum_of_letters = 0
for letters in range(lines):
    current_letter = ord(input())
    sum_of_letters += current_letter

print(f"The sum equals: {sum_of_letters}")
