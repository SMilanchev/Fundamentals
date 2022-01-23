

def validate_key(dictionary, key, def_value=" "):
    if key not in dictionary:
        dictionary[key] = def_value



def print_result(dictionary, template):
    for key, value in dictionary.items():
        print(template.format(key, value))