import os
def deletes(paths):
    if not isinstance(paths, str):
        print('not input')
        return
    if os.path.exists(paths):
        if os.access(paths, os.W_OK):
            os.remove(paths)
            print(paths,'has been deleted')
        else:
            print('not possible')
    else:
        print('doesnt exist')
paths= "/Users/danarasid/Desktop/pp2_labs/lab8/1.py"
deletes(paths)
