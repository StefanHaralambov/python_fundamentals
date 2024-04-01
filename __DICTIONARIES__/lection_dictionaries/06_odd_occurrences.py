sen = input().split()
odd_words = {}

for i in range(len(sen)):
    sen[i] = sen[i].lower()
    if sen[i] not in odd_words:
        odd_words[sen[i]] = 0
    odd_words[sen[i]] += 1

for (key, value) in odd_words.items():
    if value % 2 != 0:
        print(key, end=" ")
