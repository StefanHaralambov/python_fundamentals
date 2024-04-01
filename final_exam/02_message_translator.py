import re

count = int(input())
lss_pattern = r"(\!)([A-Z*1][a-z]{2,})(\1)(\:)(\[)([a-zA-Z]{8,})(\])"
final = []

for i in range(count):
    word = input()
    result = re.search(lss_pattern, word)
    if result:
        command = result.group(2)
        final_word = result.group(6)
    else:
        final.append("The message is invalid")
        continue

    res = f"{command}:"
    for char in final_word:
        res += f" {ord(char)}"
    final.append(res)

print("\n".join(final))
