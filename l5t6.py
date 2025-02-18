import re
with open("row.txt", "r", encoding="utf-8") as file:
    content=file.read()

mod_content=re.sub(r"[ ,.]", ":", content)

print(mod_content)