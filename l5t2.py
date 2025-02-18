import re
with open("row.txt", "r", encoding="utf-8") as file:
    for linenum, line in enumerate(file, 1):
        matches = re.findall(r"ab{2,3}", line)

        if matches:
            print(f"совпaдение в строке {linenum}: {matches}")