import os 

def sort_by_extension(director):
    res = []

    for file in os.listdir(director):
        if os.path.isfile(os.path.join(director, file)):
            res.append(file)

    # extract extensions
    ext = set()
    for file in res:
        ext.add(file[file.rfind('.'):])
    return sorted(ext)

def main():
    director = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex1"
    print(sort_by_extension(director))

if __name__ == "__main__":
    main()