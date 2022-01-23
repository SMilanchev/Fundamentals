my_dict = {1: ["niki", "Goso"], 3: ["Vanio", "Goso", "Vanio"]}
all_users = [item for current_list in my_dict.values() for item in current_list]
print(all_users)