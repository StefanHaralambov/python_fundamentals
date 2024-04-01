import re

command = input()

pattern = r"(\#|\@)([a-zA-Z]{3,})\1(\#|\@)([a-zA-Z]{3,})\1"

word_list = re.finditer(pattern, command)

words = []
mirror_words = []
pairs = 0

for word in word_list:
    words.append(word.group(2))
    words.append(word.group(4))

pairs = int(len(words) / 2)

if pairs:
    print(f"{pairs} word pairs found!")
else:
    print("No word pairs found!")

for i in range(0, len(words), 2):
    if words[i] == words[i + 1][::-1]:
        mirror_words.append(words[i])
        mirror_words.append(words[i + 1])

if mirror_words:
    print("The mirror words are:")
    for index in range(0, len(mirror_words), 2):
        if index < len(mirror_words) - 2:
            print(f"{mirror_words[index]} <=> {mirror_words[index + 1]}", end=", ")
        else:
            print(f"{mirror_words[index]} <=> {mirror_words[index + 1]}")
else:
    print("No mirror words!")
