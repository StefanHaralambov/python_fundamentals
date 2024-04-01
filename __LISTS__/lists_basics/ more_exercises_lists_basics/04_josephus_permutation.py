def solution(some_list, k):
    terminated = []
    # Calculate the initial index from where execution starts
    index = (k - 1) % len(some_list)

    while some_list:
        # Pop the person at the current index from the list and append to the executed_people list
        terminated.append(some_list.pop(index))
        if some_list:
            # current index + the step in order to continue the circle
            index = (index + k - 1) % len(some_list)
    return ",".join(terminated)


list_of_people = input().split()
targets = int(input())
print(f"[{solution(list_of_people, targets)}]")
