number = float(input())
condition = ""

if number == 0:
    condition = "zero"
elif 0 < number < 1:
    condition = "small positive"
elif 1 <= number <= 1_000_000:
    condition = "positive"
elif number > 1_000_000:
    condition = "large positive"
elif 0 < abs(number) < 1:
    condition = "small negative"
elif 1 <= abs(number) <= 1_000_000:
    condition = "negative"
elif abs(number) > 1_000_000:
    condition = "large negative"

print(condition)
