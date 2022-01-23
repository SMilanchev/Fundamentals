input_string = input()
list_from_string = []
counter = 0
for i in range(len(input_string)):
    if input_string[i].isdigit() and i+1 < len(input_string) and input_string[i+1].isdigit():
        number = int(input_string[i] + input_string[i+1])
    elif input_string[i].isdigit():
        number = int(input_string[i])
        list_from_string.append(input_string[counter:i].upper() * number)
        counter = i + len(str(number))

print(f"Unique symbols used: {len(set(''.join(list_from_string)))}\n{''.join(list_from_string)}")



