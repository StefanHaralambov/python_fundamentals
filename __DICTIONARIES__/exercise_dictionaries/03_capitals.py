countries = [x for x in input().split(", ")]
capitals = [y for y in input().split(", ")]

dict_countries_capitals = {}
dcc = dict_countries_capitals

for item in range(len(capitals)):
    key = countries[item]
    value = capitals[item]
    dcc[key] = value

for k, v in dcc.items():
    print(f"{k} -> {v}")
