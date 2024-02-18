import math

employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())

students_count = int(input())

employee_efficiency = employee_1 + employee_2 + employee_3

hours_count = math.ceil(students_count / employee_efficiency)

employee_breaks = math.floor(students_count / employee_efficiency / 3)

hours_count += employee_breaks

print(f"Time needed: {hours_count}h.")
