import re

with open("row.txt", "r", encoding="utf-8") as file:
    content = file.read()

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    
    camel_case_str = components[0] + ''.join(word.capitalize() for word in components[1:])
    
    return camel_case_str

lines = content.splitlines()

camel_case_lines = [snake_to_camel(line) for line in lines]

for line in camel_case_lines:
    print(line)
