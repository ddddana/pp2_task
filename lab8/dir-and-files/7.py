def copy(source_path, destination_path):
    with open(path1, 'r') as source_file:
        content = source_file.read()

    with open(path2, 'w') as destination_file:
        destination_file.write(content)

    print(f"Content from '{path1}' has been copied to '{path2}'.")

path1 = "/Users/danarasid/Desktop/pp2_labs/lab8/dir-and-files/7_path1.txt"
path2 = "/Users/danarasid/Desktop/pp2_labs/lab8/dir-and-files/7_path2.txt"

copy(path1, path2)
