import re

def camel_to_snake(camel_str):
    snake_case_str = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_str).lower()
    return snake_case_str

with open("row.txt", "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

for line in lines:
    snake_case_str = camel_to_snake(line)
    print("Snake Case:", snake_case_str)
