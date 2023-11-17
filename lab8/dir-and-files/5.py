def fu(path, list):
    with open(path, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')

    print(f"List has been written to the file '{path}'.")

path = "/Users/danarasid/Desktop/pp2_labs/lab8/dir-and-files/5t.txt"

str1 = ['broccoli brussels, sprout, meat']

fu(path, str1)

