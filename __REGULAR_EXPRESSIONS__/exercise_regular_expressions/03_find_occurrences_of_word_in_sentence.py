import re

sentence = input()
targeted_word = input()

pattern = fr"(?i)(\b{targeted_word}\b)"

result = re.findall(pattern, sentence)

print(len(result))
