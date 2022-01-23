import re

user = r"( |^)[a-z0-9]+([\-\_\.][a-z]+)*"
host = r"[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+"

pattern = rf"{user}@{host}"

text = input()
matches = re.finditer(pattern, text)
for match in matches:
    print(str(match[0].strip()))
