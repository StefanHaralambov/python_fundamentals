students = {}

while True:
    details = input().split(":")
    if "_" in details[0] or details[0].islower():
        break
    name, identification, course = details[0], int(details[1]), details[2]

    if course not in students:
        students[course] = {}
    students[course][identification] = name

target = " ".join(details[0].split("_"))

for key, value in students.items():
    if key == target:
        for identification, name in value.items():
            print(f"{name} - {identification}")
