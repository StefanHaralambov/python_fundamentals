# lines = int(input())
#
# is_balanced = True
# opening_brackets = 0
#
# closing_brackets = 0
# checker = ""
#
# for x in range(lines):
#     symbol = input()
#
#     if symbol == "(":
#         opening_brackets += 1
#         checker += symbol
#     elif symbol == ")":
#         closing_brackets += 1
#         checker += symbol
#     else:
#         continue
#
# if opening_brackets != closing_brackets:
#     is_balanced = False
#
# if checker == "":
#     is_balanced = False
#
# for brackets in range(len(checker)):
#     if checker[brackets] == "(" or checker == ")":
#         if checker[brackets] == len(checker):
#             break
#         if checker[brackets + 1] == "(" or checker == ")":
#             is_balanced = False
#             break
#
# if is_balanced:
#     print("BALANCED")
# else:
#     print("UNBALANCED")

qty_lines = int(input())

is_balanced = True
open_bracket = False

for lines in range(qty_lines):
    symbol = input()

    if symbol == '(':
        if open_bracket:
            is_balanced = False
        else:
            open_bracket = True
    elif symbol == ')':
        if not open_bracket:
            is_balanced = False
        else:
            open_bracket = False
    else:
        pass

if is_balanced:
    print(f'BALANCED')
else:
    print(f'UNBALANCED')
