neighborhood = [int(x) for x in input().split("@")]

last_position = 0

command = input().split()

while command[0] != "Love!":
    target_index = int(command[1])
    next_position = last_position + target_index
    last_position = next_position
    if next_position > len(neighborhood) - 1:
        next_position = 0
        last_position = 0
    if neighborhood[next_position] == 0:
        print(f"Place {next_position} already had Valentine's day.")
        command = input().split()
        continue
    neighborhood[next_position] -= 2
    if neighborhood[next_position] == 0:
        print(f"Place {next_position} has Valentine's day.")
    command = input().split()

failed_houses = 0
success = True

for houses in neighborhood:
    if houses != 0:
        failed_houses += 1
        success = False

if success:
    print(f"Cupid's last position was {last_position}.\n"
          f"Mission was successful.\n")
else:
    print(f"Cupid's last position was {last_position}.\n"
          f"Cupid has failed {failed_houses} places.")
