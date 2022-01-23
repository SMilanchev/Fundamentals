command_list = [1, 2, 3, 4, 5, 6, 7]
command_list.pop(6)

for i in range(len(command_list)):

    print(i)
    command_list.pop(int(i))

print(command_list)
