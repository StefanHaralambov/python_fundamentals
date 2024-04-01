import re

text = input()
pattern = "1"
result = re.findall(pattern, text)

int_result = [int(i) for i in result]

x = sum(int_result)

print(x)