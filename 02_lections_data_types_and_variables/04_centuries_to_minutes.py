unit = int(input())

years = unit * 100
days = years * 365.2422
hours = days * 24
minutes = hours * 60

print(f"{unit} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")
