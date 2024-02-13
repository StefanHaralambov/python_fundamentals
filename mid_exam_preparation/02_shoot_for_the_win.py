targets = input().split()

command = input()

while command != "End":
    command = int(command)
    if int(command) in range(len(targets)):
        substraction = 0
        print(substraction)
        targets[command] = "-1"
        print(targets)
    else:
        print("False")

    command = input()




