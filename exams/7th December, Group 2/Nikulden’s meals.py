def validate_guest(dict, user):
    if user not in dict.keys():
        dict[user] = []


dishes = input()
meals_liked = {}
counter_unliked_meals = 0

while dishes != "Stop":
    dishes_split = dishes.split("-")
    command = dishes_split[0]
    guest = dishes_split[1]
    meal = dishes_split[2]
    if command == "Like":
        validate_guest(meals_liked, guest)
        if meal not in meals_liked[guest]:
            meals_liked[guest].append(meal)
    elif command == "Unlike":
        if guest not in meals_liked.keys():
            print(f"{guest} is not at the party.")
        elif meal not in meals_liked[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        elif meal in meals_liked[guest]:
            counter_unliked_meals += 1
            meals_liked[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
    dishes = input()

meals_liked = dict(sorted(meals_liked.items(), key=lambda x: (-len(x[1]), x[0])))
for k, v in meals_liked.items():
    print(f"{k}: {', '.join(v)}")
print(f"Unliked meals: {counter_unliked_meals}")
