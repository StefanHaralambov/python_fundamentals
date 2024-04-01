command = input()
is_close = True
a = command.split(", ")
a.reverse()

if a.index("wolf") == 0:
    is_close = False

sheep_position = (a.index("wolf") - 1) + 1

if not is_close:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")

# wolf, sheep, sheep, sheep, sheep, sheep
