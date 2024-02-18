friend_list = input().split(", ")

banned_names_count = 0
lost_names_count = 0

command = input().split()

while command[0] != "Report":

    if command[0] == "Blacklist":
        type_, name = command[0], command[1]
        if name in friend_list:
            index = friend_list.index(name)
            friend_list[index] = "Blacklisted"
            banned_names_count += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    if command[0] == "Error":
        error, index_error = command[0], int(command[1])
        if 0 <= index_error < len(friend_list):
            name_error = friend_list[index_error]
            if index_error in range(len(friend_list)):
                if friend_list[index_error] != "Blacklisted" and friend_list[index_error] != "Lost":
                    friend_list[index_error] = "Lost"
                    lost_names_count += 1
                    print(f"{name_error} was lost due to an error.")

    if command[0] == "Change":
        change, index_change, new_name = command[0], int(command[1]), command[2]
        if 0 <= index_change < len(friend_list):
            if index_change in range(len(friend_list)):
                current_name = friend_list[index_change]
                friend_list[index_change] = new_name
                print(f"{current_name} changed his username to {new_name}.")

    command = input().split()

print(f"Blacklisted names: {banned_names_count}")
print(f"Lost names: {lost_names_count}")
print(*friend_list, sep=" ")
