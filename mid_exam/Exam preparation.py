pirate_ship = input().split(">")
pirate_ship_status = list(map(lambda x: int(x), pirate_ship))
warship = input().split(">")
warship_status = list(map(lambda x: int(x), warship))
max_health = int(input())
game_over = False

line = input()
while line != "Retire":
    line_list = line.split()
    command = line_list[0]
    if command == "Fire":
        index = int(line_list[1])
        damage = int(line_list[2])
        if index >= len(warship_status) or index < 0:
            pass
        else:
            warship_status[index] = warship_status[index] - damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                game_over = True
                break
    elif command == "Defend":
        start_index = int(line_list[1])
        end_index = int(line_list[2])
        damage = int(line_list[3])
        if start_index < 0 or end_index >= len(pirate_ship_status) \
                or start_index >= len(pirate_ship_status) or end_index < 0:
            pass
        else:
            for i in range(start_index, end_index + 1):
                pirate_ship_status[i] = pirate_ship_status[i] - damage
                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    game_over = True
                    break
    elif command == "Repair":
        index = int(line_list[1])
        health = int(line_list[2])
        if index < 0 or index >= len(pirate_ship_status):
            pass
        else:
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health:
                pirate_ship_status[index] = max_health
    elif command == "Status":
        sections_to_repair = [element for element in pirate_ship_status \
                              if element < 0.2 * max_health]
        print(f"{len(sections_to_repair)} sections need repair.")
    line = input()
    if line == "Retire" and game_over is not True:
        print(f"Pirate ship status: {sum(pirate_ship_status)}")
        print(f"Warship status: {sum(warship_status)}")


