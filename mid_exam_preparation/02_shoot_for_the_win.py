targets = [int(target) for target in input().split()]

target_down = 0

command = input()

while command != "End":
    target_index = int(command)

    if target_index in range(len(targets)):
        for index in range(len(targets)):
            if targets[index] == -1:
                continue
            if target_index == index:
                continue
            if targets[target_index] < targets[index]:
                targets[index] -= targets[target_index]

            else:
                targets[index] += targets[target_index]
        targets[target_index] = -1
        target_down += 1

    command = input()

result = " ".join(map(str, targets))

print(f"Shot targets: {target_down} -> {result}")
