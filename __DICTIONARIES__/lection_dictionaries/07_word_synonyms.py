times = int(input())
list_of_words = {}

for i in range(times):
    word = input()
    syn = input()
    if word not in list_of_words:
        list_of_words[word] = [syn]
    else:
        list_of_words[word].append(syn)

for (key, value) in list_of_words.items():
    val = ", ".join(map(str, value))
    print(f"{key} - {val}")
