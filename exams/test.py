dict = {"ivan": "gei", "niki": "Ivan", "gonzo": "ne usm gei"}
dict = sorted(dict.items(), key=lambda x: -len(x[1]))
print(dict)