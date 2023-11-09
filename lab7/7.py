import re

def text_match(text):
         return ''.join(x.capitalize() or '_' for x in text.split('_'))
        
with open("row.txt","r") as file:
    text = file.read()

print(text_match(text))