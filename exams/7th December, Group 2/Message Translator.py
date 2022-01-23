import re

messages_number = int(input())
pattern = r"!(?P<command>[A-Z][a-z]{2,})!:\[(?P<message>[a-zA-Z]{8,})]"

for i in range(messages_number):
    message = input()
    match = re.match(pattern, message)
    if match is None:
        print("The message is invalid")
        continue
    print(f"{match[1]}:", end=" ")
    for element in match[2]:
        if element == " ":
            continue
        print(ord(element), end=" ")
    print()


