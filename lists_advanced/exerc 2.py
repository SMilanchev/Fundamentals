def time(list):
    seconds = 0
    seconds_two = 0
    for i in range(mid):
        seconds = seconds + list_nums[i]
        if list_nums[i] == 0:
            seconds = seconds * 0.8
    for m in range(mid + 1, len(list_nums)):
        seconds_two = seconds_two + list_nums[m]
        if list_nums[m] == 0:
            seconds_two = seconds_two * 0.8
    if seconds < seconds_two:
        return f"The winner is left with total time: {seconds:.1f}"
    else:
        return f"The winner is right with total time: {seconds_two:.1f}"


list_str = input().split()
list_nums = list(map(lambda x: int(x), list_str))
mid = int(len(list_nums) / 2)
print(time(list_str))

