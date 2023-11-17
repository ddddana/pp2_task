import os

def fu(path):
    items = os.listdir(path)

    print(f"Contents of {path}:")

    for item in items:
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            print(f"Directory: {item}")
       
        elif os.path.isfile(item_path):
            print(f"File: {item}")
        
        else:
            print(f"Item: {item}")

path1 = "/Users/danarasid/Desktop/pp2_labs"

fu(path1)
