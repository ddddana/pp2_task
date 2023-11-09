import re
pattern = r'ab{2,3}'
with open("row.txt","r") as file:
    text = file.read()

x=re.findall(pattern, text)
if x:
    print(f"Found a match!")
else:
    print(f"Not matched!")