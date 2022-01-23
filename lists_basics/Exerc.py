rows = int(input())
nums = []

for j in range(1, rows + 1):
    string = input().split()
    for element in string:
        nums.append(int(element))

