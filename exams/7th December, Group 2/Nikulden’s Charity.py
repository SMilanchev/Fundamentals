string = input()

while True:
    command = input()
    if command == "Finish":
        break
    command = command.split()
    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        string = string.replace(current_char, new_char)
        print(string)
    elif command[0] == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index >= len(string) or end_index >= len(string) or start_index < 0 or end_index < 0:
            print("Invalid indexes!")
            continue
        string = string[0:start_index] + string[end_index+1:]
        print(string)
    elif command[0] == "Make":
        if command[1] == "Upper":
            string = string.upper()
        else:
            string = string.lower()
        print(string)
    elif command[0] == "Check":
        message = command[1]
        if message in string:
            print(f"Message contains {message}")
            continue
        print(f"Message doesn't contain {message}")
        continue
    elif command[0] == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index >= len(string) or end_index >= len(string) or start_index < 0 or end_index < 0:
            print("Invalid indexes!")
            continue
        sum = 0
        for i in string[start_index:end_index+1]:
            sum += ord(i)
        print(sum)
