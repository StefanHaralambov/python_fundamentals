import re

regex = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"

test_str = input()

matches = re.finditer(regex, test_str)

destinations = []
points = 0

for destination in matches:
    destinations.append(destination.group(2))
    points += len(destination.group(2))

print(f"Destinations: {', '.join(destinations)}\nTravel Points: {points}")
