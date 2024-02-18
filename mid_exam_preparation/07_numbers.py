nums = [int(x) for x in input().split()]

average_num = sum(nums) / len(nums)
top_nums = []

less_average = 0
above_nums = 0

for number in nums:
    if number > average_num:
        top_nums.append(number)
        above_nums += 1
    elif number <= average_num:
        less_average += 1

top_nums.sort()
reversed_nums = top_nums[-1: -6: -1]
print(*reversed_nums, sep=" ")

if above_nums == 0:
    print("No")



