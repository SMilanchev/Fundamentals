def validate_key(dictionary, key):
    if key not in dictionary:
        dictionary[key] = []


users = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        command = command.split(" | ")
        side = command[0]
        user = command[1]
        validate_key(users, side)
        if user not in users[side]:
            users[side].append(user)
    elif "->" in command:
        command = command.split(" -> ")
        user = command[0]
        side = command[1]
        for k, v in users.items():
            if user in v:
                users[k].remove(user)
        validate_key(users, side)
        users[side].append(user)
        print(f"{user} joins the {side} side!")

users_sorted = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))
for k, v in users_sorted.items():
    if len(v) == 0:
        continue
    else:
        print(f"Side: {k}, Members: {len(v)}")
        for i in sorted(v):
            print(f"! {i}")