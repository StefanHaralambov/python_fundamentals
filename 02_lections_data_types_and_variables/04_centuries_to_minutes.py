unit = int(input())

# ⦁	Assume that one year has 365.2422 days on average

years = unit * 100
days = round(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{unit} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
