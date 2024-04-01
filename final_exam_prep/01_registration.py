username = input()

while True:
    command = input().split()
    current_command = command[0]
    if current_command == "Registration":
        break

    if current_command == "Letters":
        case = command[1]
        if case == "Upper":
            username = username.upper()
            print(username)
            continue
        elif case == "Lower":
            username = username.lower()
            print(username)
            continue

    if current_command == "Reverse":
        start, end = int(command[1]), int(command[2])
        if 0 <= start < len(username) and 0 <= end < len(username):
            reversed_user = username[start: end + 1][::-1]
            print(reversed_user)
            continue
        else:
            continue

    if current_command == "Substring":
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
            continue
        else:
            print(f"The username {username} doesn't contain {substring}.")
            continue

    if current_command == "Replace":
        char = command[1]
        username = username.replace(char, "-")
        print(username)
        continue

    if current_command == "IsValid":
        target_char = command[1]
        if target_char in username:
            print("Valid username.")
        else:
            print(f"{target_char} must be contained in your username.")
