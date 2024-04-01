targets = [int(number) for number in input().split()]

command = input().split()

while command[0] != "End":
    type_command, index, action = command[0], int(command[1]), int(command[2])

    if type_command == "Shoot":
        if index not in range(len(targets)):
            command = input().split()
            continue
        targets[index] -= action
        if targets[index] <= 0:
            targets.pop(index)

    elif type_command == "Add":
        if index not in range(len(targets)):
            print("Invalid placement!")
            command = input().split()
            continue
        else:
            targets.insert(index, action)

    elif type_command == "Strike":
        if index - action >= 0 and index + action < len(targets):
            del targets[index - action: index + action + 1]
        else:
            print("Strike missed!")
            command = input().split()
            continue

    command = input().split()

print(*targets, sep="|")
