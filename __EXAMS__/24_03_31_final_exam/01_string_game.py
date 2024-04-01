text = input()

while True:
    command = input().split()
    current_command = command[0]

    if current_command == "Done":
        break

    if current_command == "Change":
        char, replacement = command[1], command[2]
        for i in range(len(text)):

            if char == text[i]:
                text = text.replace(char, replacement)
        print(text)

    if current_command == "Includes":
        substring = command[1]

        if substring in text:
            print("True")
        else:
            print("False")

    if current_command == "End":
        substring = command[1]

        if text.endswith(substring):
            print("True")
        else:
            print("False")

    if current_command == "Uppercase":
        text = text.upper()
        print(text)

    if current_command == "FindIndex":
        target_char = command[1]
        result = text.index(target_char)
        print(result)

    if current_command == "Cut":
        start, count = int(command[1]), int(command[2])
        text = text[start: start + count: 1]
        print(text)
