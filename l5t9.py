import re

with open("row.txt", "r", encoding="utf-8") as file:
    content = file.read()

def insert_spaces(s):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)

lines = content.splitlines()

for line in lines:
    split_str = insert_spaces(line)
    print("Split string:", split_str)
