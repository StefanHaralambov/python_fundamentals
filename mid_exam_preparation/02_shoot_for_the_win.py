targets = [int(target) for target in input().split()]

target_down = 0

command = input()

while command != "End":
    target_index = int(command)

    if target_index in range(len(targets)):
        for index in range(len(targets)):
            current_target_points, aimed_target = targets[index], targets[target_index]
            if current_target_points == -1:
                continue
            if target_index == index:
                continue
            if aimed_target < current_target_points:
                current_target_points -= aimed_target

            else:
                current_target_points += aimed_target
        aimed_target = -1
        target_down += 1

    command = input()

result = " ".join(map(str, targets))

print(f"Shot targets: {target_down} -> {result}")
