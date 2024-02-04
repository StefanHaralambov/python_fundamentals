command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    for char in command:
        print(f"{char}" * 2, end="")
    command = input()
