initial_energy = int(input())

command = input()

won_battles = 0
have_energy = True

while command != "End of battle":
    distance = int(command)
    if initial_energy < distance:
        have_energy = False
        break

    if initial_energy == 0:
        have_energy = False
        break

    initial_energy -= distance
    won_battles += 1

    if won_battles % 3 == 0:
        initial_energy += won_battles

    command = input()

if not have_energy:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
