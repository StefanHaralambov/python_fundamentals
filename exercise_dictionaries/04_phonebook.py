phonebook = {}

command = input().split("-")

while len(command) != 1:
    key = command[0]
    value = command[1]
    if key not in phonebook:
        phonebook[key] = value
    else:
        phonebook.update({key: value})
    command = input().split("-")

for name in range(int(command[0])):
    get_name = input()
    if get_name in phonebook.keys():
        print(f"{get_name} -> {phonebook[get_name]}")
    else:
        print(f"Contact {get_name} does not exist.")
