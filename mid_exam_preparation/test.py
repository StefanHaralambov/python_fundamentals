list1 = ["10", "20", "30", "40"]
int_lst = [int(x) for x in list1]
print(int_lst)
integer = int(input())

for i in range(len(int_lst)):
    if int_lst[i] > integer:
        int_lst[i] += integer
        print(i)
