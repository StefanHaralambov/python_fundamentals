command = input()
text = {}

for i in range(len(command)):
    if command[i] == " ":
        continue
    elif command[i] not in text:
        text[command[i]] = 1
    else:
        text[command[i]] += 1

for k, v in text.items():
    print(f"{k} -> {v}")
