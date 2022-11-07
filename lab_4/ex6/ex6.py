import os

def file_search(file, to_search, callback):
    try:
        f = open(file).read()
        if to_search in f:
            return [os.path.relpath(file)]
    except Exception as e:
        callback(e)
    return []

def directory_search(director, to_search, callback):
    res = []
    for (r, d, f) in os.walk(director):
        for file in f:
            try:
                content = open(os.path.join(director,file)).read()
                if to_search in content:
                    res.append(file)
            except Exception as e:
                callback(e)
    return res

def search(target, to_search, callback):
    if os.path.isfile(target):
        return file_search(target, to_search, callback)
    if os.path.isdir(target):
        return directory_search(target, to_search, callback)
    raise ValueError("Neither directory nor file!")


def main():
    director = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files.d"
    fisier = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files/test.txt"

    to_search = "string"
    callback = lambda error : print(error)
    print(search(fisier, to_search, callback))
    print(search(director, to_search, callback))

if __name__ == "__main__":
    main()