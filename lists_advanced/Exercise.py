list_nums = [29, 13, 9, 0, 13, 0, 21, 0, 14, 82, 12]
mid = int(len(list_nums) / 2)


def time(list):
    seconds = 0
    for i in range(mid):
        seconds = seconds + list_nums[i]
        if list_nums[i] == 0:
            seconds = seconds * 0.8
    return seconds


second = list_nums[::-1]
second_time = time(second)
print(second_time)
