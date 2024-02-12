input_year = int(input())
happy_year = input_year
found_next_year = False

while not found_next_year:
    happy_year += 1
    if len(str(happy_year)) == len(set(str(happy_year))):
        found_next_year = True

print(f'{happy_year}')
