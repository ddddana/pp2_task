import os

def check_path_and_extract_info(path):

    if os.path.exists(path):
        print(f"Path '{path}' exists.")

        directory_name, file_name = os.path.split(path)

        print(f"Directory Name: {directory_name}")
        print(f"File Name: {file_name}")
    else:
        print(f"Path '{path}' does not exist.")

path_to_check = "/Users/danarasid/Desktop/pp2_labs/lab8"

check_path_and_extract_info(path_to_check)
