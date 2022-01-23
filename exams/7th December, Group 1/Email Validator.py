email = input()

while True:
    command = input()
    if command == "Complete":
        break
    command_split = command.split()
    if command_split[0] == "Make":
        if command_split[1] == "Upper":
            email = email.upper()
        else:
            email = email.lower()
        print(email)
    elif command_split[0] == "GetDomain":
        count = int(command_split[1])
        print(email[-count:])
    elif command_split[0] == "GetUsername":
        if "@" in email:
            print(email[:email.index("@")])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
            continue
    elif command_split[0] == "Replace":
        char = command_split[1]
        email = email.replace(char, "-")
        print(email)
    elif command_split[0] == "Encrypt":
        email = [str(ord(element)) for element in email]
        print(" ".join(email))