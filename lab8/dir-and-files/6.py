for char in range(ord('A'), ord('Z')+1):
    files= chr(char) +'.txt'
    with open(files,'w') as file:
        file.write(files)
    print(files)

