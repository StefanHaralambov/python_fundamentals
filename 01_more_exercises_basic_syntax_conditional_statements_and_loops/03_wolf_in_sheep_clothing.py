command = input()
word = ""
animals = []

for letters in command:
    if letters == ",":
        continue
    elif letters == " ":
        continue
    if word == "wolf":
        animals.append("wolf")
        word = ""
        word += letters
        continue
    elif word == "sheep":
        animals.append("sheep")
        word = ""
        word += letters
        continue
    word += letters

print(animals)
