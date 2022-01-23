def email_validator(dict, user):
    if user not in dict.keys():
        dict[user] = []
    else:
        print(f"{user} is already registered")


emails_sent = {}
while True:
    command = input().split("->")
    if command[0] == "Statistics":
        break
    username = command[1]
    if command[0] == "Add":
        email_validator(emails_sent, username)
    elif command[0] == "Send":
        email = command[2]
        emails_sent[username].append(email)
    elif command[0] == "Delete":
        if username in emails_sent.keys():
            emails_sent.pop(username)
        else:
            print(f"{username} not found!")

emails_sorted = dict(sorted(emails_sent.items(), key=lambda x: (-len(x[1]), x[0])))
print(f"Users count: {len(emails_sorted)}")
for key, value in emails_sorted.items():
    print(key, value)
    print(key)
    for v in value:
        print(f" - {v}")
