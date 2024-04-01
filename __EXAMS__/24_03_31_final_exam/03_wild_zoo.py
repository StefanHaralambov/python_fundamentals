stefan_dict = {}
stf_dict2 = {}

while True:
    command = input()
    if command == "EndDay":
        break

    command, command_2 = command.split(": ")

    if command == "Add":
        command_2 = command_2.split("-")
        name = command_2[0]
        needed_food = int(command_2[1])
        area = command_2[2]

        if name not in stefan_dict.keys():
            stefan_dict[name] = {"food": needed_food, "area": area}
        elif name in stefan_dict.keys():
            stefan_dict[name]["food"] += needed_food

    elif command == "Feed":
        command_2 = command_2.split("-")
        name = command_2[0]
        food = int(command_2[1])

        if name in stefan_dict.keys():
            stefan_dict[name]["food"] -= food

            if stefan_dict[name]["food"] <= 0:
                print(f"{name} was successfully fed")
                del stefan_dict[name]

print("Animals:")

for names, vals in stefan_dict.items():
    print(f" {names} -> {vals['food']}g")

    if vals['area'] not in stf_dict2:
        stf_dict2[vals['area']] = 1

    elif vals['area'] in stf_dict2:
        stf_dict2[vals['area']] += 1

print("Areas with hungry animals:")

for k, v in stf_dict2.items():
    print(f' {k}: {v}')

