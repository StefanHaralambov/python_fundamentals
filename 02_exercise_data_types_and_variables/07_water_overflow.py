number_of_lines = int(input())

water_tank_capacity = 255
liters_in_tank = 0
for _ in range(number_of_lines):
    quantity_of_water = int(input())
    liters_in_tank += quantity_of_water
    if liters_in_tank > water_tank_capacity:
        liters_in_tank -= quantity_of_water
        print("Insufficient capacity!")
        continue

print(liters_in_tank)
