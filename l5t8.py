import re

with open("row.txt", "r", encoding="utf-8") as file:
    content = file.read()

def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

lines = content.splitlines()

for line in lines:
    split_str = split_at_uppercase(line)
    print("Split string:", split_str)
