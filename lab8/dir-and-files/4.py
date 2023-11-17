import os
def counts(path):
    if os.path.exists(path):
        with open(path, 'r') as file:
            line_count= sum(1 for line in file)
        return line_count
    else:
        return "not found"
path= "/Users/danarasid/Desktop/pp2_labs/lab8/dir-and-files/4t.txt"
lines= counts(path)
if isinstance(lines, int):
    print(lines)
else:
    print(lines)


