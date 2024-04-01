initial_budget = int(input())
budget = initial_budget
enought_money = True

command = input()
while command != "End":
    budget -= int(command)
    if budget < 0:
        enought_money = False
        break
    command = input()
if not enought_money:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")
