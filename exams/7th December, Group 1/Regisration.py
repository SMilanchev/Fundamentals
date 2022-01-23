import re

inputs_number = int(input())
pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([a-zA-Z]{5,}\d+)P@\$"
counter = 0

for i in range(inputs_number):
    registration = input()
    match = re.match(pattern, registration)
    if match:
        print("Registration was successful")
        print(f"Username: {match.group(1)}, Password: {match.group(2)}")
        counter += 1
    else:
        print("Invalid username or password")

print(f"Successful registrations: {counter}")
