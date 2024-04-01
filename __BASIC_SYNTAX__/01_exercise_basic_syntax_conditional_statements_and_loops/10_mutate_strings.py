first_word = input()  # Kitty
second_word = input()  # Doggy

current_word = first_word

for letters in range(len(first_word)):
    left_side = second_word[:letters + 1]
    right_side = first_word[letters + 1:]

    new_word = left_side + right_side

    if new_word != current_word:
        print(left_side + right_side)

    current_word = new_word
