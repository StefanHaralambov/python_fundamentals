items = []
counter = 0
resources = {}

while True:
    command = input()

    if command == "stop":
        break

    items.append(command)

for item in range(0, len(items), 2):
    key = items[item]
    value = items[item + 1]
    if key not in resources:
        resources[key] = int(value)
    else:
        resources[key] += int(value)

for k, v in resources.items():
    print(f"{k} -> {v}")
