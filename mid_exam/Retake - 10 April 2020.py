number_cars = int(input())
cars_list = []
for _ in range(number_cars):
    cars_list.append(input().split("|"))
is_continue = True

line = input()
while is_continue:
    line_list = line.split(" : ")
    command = line_list[0]
    car = line_list[1]

    if command == "Drive":
        distance = int(line_list[2])
        fuel = int(line_list[3])
        for element in cars_list:
            if car in element:
                if int(element[2]) < fuel:
                    print("Not enough fuel to make that ride")
                else:
                    element[2] = str(int(element[2]) - fuel)
                    element[1] = str(int(element[1]) + distance)
                    print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                    if int(element[1]) >= 100000:
                        print(f"Time to sell the {car}!")
                        cars_list.remove(element)
    elif command == "Refuel":
        fuel = int(line_list[2])
        for element in cars_list:
            if car in element:
                first_liters = int(element[2])
                element[2] = str(int(element[2]) + fuel)
                if int(element[2]) > 75:
                    fuel = 75 - first_liters
                    element[2] = "75"
                print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        kilometers = int(line_list[2])
        for element in cars_list:
            if car in element:
                element[1] = str(int(element[1]) - kilometers)
                if int(element[1]) < 10000:
                    element[1] = "10000"
                else:
                    print(f"{car} mileage decreased by {kilometers} kilometers")

    line = input()
    if line == "Stop":
        is_continue = False


def take_second_element(ele):
    return int(ele[1])


cars_list.sort(key=take_second_element, reverse=True)
for elements in cars_list:
    print(f"{elements[0]} -> Mileage: {elements[1]} kms, Fuel in the tank: {elements[2]} lt.")

