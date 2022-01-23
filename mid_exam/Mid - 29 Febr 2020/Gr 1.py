journal = input().split(", ")

line = input()
while line != "Craft!":
    line = line.split(" - ")
    command = line[0]
    if command == "Collect":
        item = line[1]
        if item not in journal:
            journal.append(item)
    elif command == "Drop":
        item = line[1]
        if item in journal:
            journal.remove(item)
    elif command == "Combine Items":
        items = line[1]
        items = items.split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index+1, new_item)
    elif command == "Renew":
        item = line[1]
        if item in journal:
            journal.remove(item)
            journal.append(item)
    line = input()

print(", ".join(journal))