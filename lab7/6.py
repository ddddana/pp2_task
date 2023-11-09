import re

def text_match(text):
        return re.sub("[ ,.]",';',text)

with open("row.txt","r") as file:
    text = file.read()

print(text_match(text))