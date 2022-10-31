import os 

def file_management(my_path):
    try:
        f = open(my_path).read()
        return f[len(f) - 20: ]
    except Exception as e:
        print(e)

def directory_management(my_path):
    # 1. Go recursively through all the items in the directory.
    ext = dict()
    for (root, directory, files) in os.walk(my_path):
        # 2. For each file, add it/count it in a dictionary.
        for file in files:
            if (os.path.isfile(os.path.join(my_path, file))):
                if file[file.rfind('.'):] not in ext.keys():
                    ext[file[file.rfind('.'):]] = 1
                else:
                    ext[file[file.rfind('.'):]] += 1
    # 3. Transform the dictionary into a list of tuples.
    res = []
    for item in ext.items():
        res.append((item[0], item[1]))
    # 4. Sort the tuple list in descending order by the count.
    res.sort(key = lambda val : val[1], reverse=True)
    return res

def file_directory(my_path):
    if os.path.isfile(my_path):
        return file_management(my_path)
    if os.path.isdir(my_path):
        return directory_management(my_path) 

def main():
    director = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files"
    fisier = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files/test.txt"
    print(file_directory(fisier))
    print(file_directory(director))

if __name__ == "__main__":
    main()