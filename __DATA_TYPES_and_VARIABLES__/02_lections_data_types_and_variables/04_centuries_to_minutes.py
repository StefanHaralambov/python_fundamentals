unit = int(input())

years = unit * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{unit} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
