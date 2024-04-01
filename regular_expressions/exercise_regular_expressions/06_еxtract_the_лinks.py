import re

pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"
text = input()
while text:

    valid_domain = re.search(pattern, text)
    if valid_domain:
        domain = valid_domain.group(1)
        print(domain)

    text = input()
